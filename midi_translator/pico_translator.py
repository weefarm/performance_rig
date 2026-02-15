import machine
import time
import usb.device
from usb.device.midi import MIDIInterface
from machine import Pin
import neopixel
import math

# --- CONFIGURATION ---
GCP_CHANNEL   = 4   # Incoming Channel for Ground Control Pro
STOCK_CHANNEL = 5   # Incoming Channel for Stock FCB1010

QC_CHANNEL    = 1    # Outgoing Channel for Quad Cortex
HRP_CHANNEL   = 2    # Outgoing Channel for HeadRush Prime
MC_CHANNEL    = 3    # Outgoing Channel for Microcosm

# --- USB MODE ---
# STRICT_MIDI = True  -> Pure MIDI device (mioXM compatible, no Thonny after boot)
# STRICT_MIDI = False -> Composite device (Thonny works, but mioXM may not see MIDI)
STRICT_MIDI = False

# --- HARDWARE ---
led = Pin("LED", Pin.OUT)
# WS2812 on GPIO 28
pixel = neopixel.NeoPixel(machine.Pin(28), 1)
midi_received = False  

# --- TRANSLATOR LOGIC ---
class RigTranslator(MIDIInterface):
    def program_change(self, ch, pc):
        self.send_event(0x0C, 0xC0 | (ch & 0x0F), pc & 0x7F, 0)

    def on_midi_event(self, cin, midi0, midi1, midi2):
        global midi_received
        midi_received = True  
        
        status = midi0 & 0xF0
        channel = midi0 & 0x0F
        
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
                # PASSTHROUGH (other channels)
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
# No custom USB name — let MicroPython use its default descriptors.
# Custom names can confuse embedded USB hosts like the mioXM.

print("Pico 2 W Translator - 5s rescue window (hit STOP in Thonny to edit)...")

# Colors (R, G, B)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Animation constants
BREATH_SPEED = 0.05
brightness = 0
angle = 0

# 1. Start with RED during the 5s rescue window
#    To edit this file later: power-cycle the Pico, connect Thonny within 5s, hit STOP.
pixel[0] = RED
pixel.write()
time.sleep(5)

# 2. Init USB MIDI (after rescue window, same as ee3e05d)
translator = RigTranslator()
usb.device.get().init(translator, builtin_driver=(not STRICT_MIDI))

# Main loop
while True:
    if midi_received:
        # High brightness BLUE blip for MIDI
        pixel[0] = BLUE
        pixel.write()
        led.on()
        time.sleep(0.1) # Quick blip
        led.off()
        midi_received = False
        # Reset angle so breath starts from bottom after a blip
        angle = 0 
    else:
        # Slow breathing GREEN
        brightness = int((math.sin(angle) + 1) * 64) 
        pixel[0] = (0, brightness, 0)
        pixel.write()
        
        # Internal LED heartbeat (keep for debugging)
        if angle % 6.28 < 0.1: led.on()
        else: led.off()
        
        angle += BREATH_SPEED
        if angle > 628: angle = 0 # Prevent float overflow
        
        time.sleep(0.02) # ~50fps animation
