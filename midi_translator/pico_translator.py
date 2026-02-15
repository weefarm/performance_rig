import machine
import time
import usb.device
from usb.device.midi import MIDIInterface
from machine import Pin

# --- CONFIGURATION ---
GCP_CHANNEL   = 4   # Incoming Channel for Ground Control Pro
STOCK_CHANNEL = 5   # Incoming Channel for Stock FCB1010

QC_CHANNEL    = 1    # Outgoing Channel for Quad Cortex
HRP_CHANNEL   = 2    # Outgoing Channel for HeadRush Prime
MC_CHANNEL    = 3    # Outgoing Channel for Microcosm

# --- USB MODE ---
# If your mioXM shows "Board in FS mode", it is talking to the Serial port.
# SET THIS TO TRUE to hide the Serial port and force a pure MIDI identity.
STRICT_MIDI = False 

# --- HARDWARE ---
led = Pin("LED", Pin.OUT)
midi_received = False  # <--- NEW: Activity flag

# --- TRANSLATOR LOGIC ---
class RigTranslator(MIDIInterface):
    def on_midi_event(self, cin, midi0, midi1, midi2):
        global midi_received
        midi_received = True  
        
        status = midi0 & 0xF0
        channel = midi0 & 0x0F
        
        # Calculate the correct packed 4-byte header (Cable Index Number << 4 | Code Index Number)
        # Most common channel messages use the status nibble as the CIN.
        # This ensures we send valid USB MIDI packets for ALL traffic.
        cin_packed = (cin << 4) | (status >> 4)
        
        # 1. Program Change (0xC0)
        if status == 0xC0:
            pc_num = midi1
            # GCP (Ch 4) -> QC (Ch 1)
            if channel == GCP_CHANNEL - 1:
                if pc_num <= 7: # PC 0-7 -> CC 35-42
                    self.control_change(QC_CHANNEL - 1, 35 + pc_num, 127)
                elif pc_num >= 8 and pc_num <= 15: # PC 8-15 -> CC 80-87
                    self.control_change(QC_CHANNEL - 1, 72 + pc_num, 127)
            # FCB (Ch 5) -> HRP (Ch 2)
            elif channel == STOCK_CHANNEL - 1:
                if pc_num <= 7: # PC 0-7 -> CC 75-82
                    self.control_change(HRP_CHANNEL - 1, 75 + pc_num, 127)
                elif pc_num == 8: # Prev
                    self.control_change(HRP_CHANNEL - 1, 17, 127)
                elif pc_num == 9: # Next
                    self.control_change(HRP_CHANNEL - 1, 16, 127)
            else:
                # PASSTHROUGH (Ch 10, etc)
                self.program_change(channel, pc_num)

        # 2. Control Change (0xB0)
        elif status == 0xB0:
            cc_num = midi1
            cc_val = midi2
            # GCP Exp (Ch 4)
            if channel == GCP_CHANNEL - 1:
                if cc_num == 1: # Wah
                    self.control_change(QC_CHANNEL - 1, 1, cc_val)
                elif cc_num == 2: # Vol
                    self.control_change(QC_CHANNEL - 1, 2, cc_val)
            # FCB Exp (Ch 5)
            elif channel == STOCK_CHANNEL - 1:
                if cc_num == 7: # Exp A
                    self.control_change(HRP_CHANNEL - 1, 61, cc_val)
                elif cc_num == 27: # Exp B
                    self.control_change(HRP_CHANNEL - 1, 62, cc_val)
            else:
                # PASSTHROUGH
                self.control_change(channel, cc_num, cc_val)

        # 3. Everything Else (Clock, SysEx, etc.)
        else:
            # Fallback for non-channel data
            try:
                self.write(0, midi0, midi1, midi2)
            except:
                pass
            

# --- STARTUP ---
# Custom USB Identity (Optional)
try:
    # On RP2350, the product string must be set via low-level config descriptors
    # Index 0x02 is the standard Product String index for MicroPython
    machine.USBDevice().config(desc_strs={0x02: "Pico 2 W Translator"})
except Exception as e:
    print("Warning: Could not set custom USB name:", e)

# RESCUE WINDOW: You have 5 seconds after power-on to hit "STOP" in Thonny.
# If you don't hit stop, and STRICT_MIDI is True, you will lose Serial access.
print("Waiting 5s for Thonny/Serial (HIT STOP NOW TO EDIT)...")
time.sleep(5)

translator = RigTranslator()
# builtin_driver=True allows Thonny to work but can confuse the mioXM.
# builtin_driver=False makes the Pico a pure MIDI device (mioXM favorite).
usb.device.get().init(translator, builtin_driver=(not STRICT_MIDI))

print("Pico 2 W Translator Active...")

# Main loop
while True:
    if midi_received:
        # Long, unmistakable pulse for MIDI events
        led.on()
        time.sleep(0.25) 
        led.off()
        midi_received = False
    else:
        # Discrete heartbeat (short blip)
        led.on()
        time.sleep(0.01)
        led.off()
        time.sleep(0.99)
