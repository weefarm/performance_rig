import machine
import time
import usb.device
from usb.device.midi import MIDIInterface
from machine import Pin
import neopixel
import math

# --- CONFIGURATION ---
GCP_CHANNEL   = 4   
STOCK_CHANNEL = 5   

QC_CHANNEL    = 1    
HRP_CHANNEL   = 2    
MC_CHANNEL    = 3    

# Global flags for LED feedback
midi_received   = False
translated_sent = False

# --- USB MODE ---
STRICT_MIDI = False # Set to True for production with mioXM

# --- HARDWARE ---
led = Pin("LED", Pin.OUT)
pixel = neopixel.NeoPixel(machine.Pin(28), 1)

# Colors
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE   = (255, 255, 255)

# --- TRANSLATOR LOGIC ---
class RigTranslator(MIDIInterface):
    def tx_translated(self, status, ch, d1, d2):
        """Sends a message and marks it as handled/magenta."""
        global translated_sent
        translated_sent = True
        if status == 0xC0:
            self.send_event(0x0C, 0xC0 | (ch & 0x0F), d1 & 0x7F, 0)
        elif status == 0xB0:
            self.control_change(ch, d1, d2)
        else:
            self.send_event(status >> 4, status | (ch & 0x0F), d1, d2)

    def tx_passthrough(self, cin, midi0, midi1, midi2):
        """Passes message through without translation flags (will flash Cyan/White)."""
        self.send_event(cin, midi0, midi1, midi2)

    def on_midi_event(self, cin, midi0, midi1, midi2):
        # global midi_received # Removed
        # midi_received = True   # Removed
        
        status = midi0 & 0xF0
        channel = midi0 & 0x0F
        
        # 1. Program Change (0xC0)
        if status == 0xC0:
            pc_num = midi1
            # --- GCP (Ch 4) -> QC (Ch 1) ---
            if channel == GCP_CHANNEL - 1:
                # Re-map first 16 buttons to Quad Cortex Scenes (80+)
                if pc_num <= 7: # PC 0-7 -> CC 80-87 (SCENES A-H)
                    self.tx_translated(0xB0, QC_CHANNEL - 1, 80 + pc_num, 127)
                    pixel[0] = (0, 255, 255) # CYAN
                elif pc_num >= 8 and pc_num <= 15: # Stomps block
                    self.tx_translated(0xB0, QC_CHANNEL - 1, 72 + pc_num, 127)
                    pixel[0] = (255, 0, 255) # MAGENTA
                else:
                    self.tx_passthrough(cin, midi0, midi1, midi2)
                    pixel[0] = (255, 255, 255) # WHITE
                pixel.write()
            
            # --- FCB (Ch 5) -> HRP (Ch 2) ---
            elif channel == STOCK_CHANNEL - 1:
                pixel[0] = (0, 255, 0) # GREEN
                pixel.write()
                if pc_num <= 7: # PC 0-7 -> CC 75-82
                    self.tx_translated(0xB0, HRP_CHANNEL - 1, 75 + pc_num, 127)
                elif pc_num == 8: # Prev
                    self.tx_translated(0xB0, HRP_CHANNEL - 1, 17, 127)
                elif pc_num == 9: # Next
                    self.tx_translated(0xB0, HRP_CHANNEL - 1, 16, 127)
                else:
                    self.tx_passthrough(cin, midi0, midi1, midi2)
            
            # --- ALL OTHER PCs ---
            else:
                self.tx_passthrough(cin, midi0, midi1, midi2)

        # 2. Control Change (0xB0)
        elif status == 0xB0:
            cc_num = midi1
            cc_val = midi2
            # --- GCP Exp (Ch 4) ---
            if channel == GCP_CHANNEL - 1:
                pixel[0] = (0, 255, 255) # CYAN
                pixel.write()
                if cc_num == 1: # Wah
                    self.tx_translated(0xB0, QC_CHANNEL - 1, 1, cc_val)
                elif cc_num == 2: # Vol
                    self.tx_translated(0xB0, QC_CHANNEL - 1, 2, cc_val)
                else:
                    self.tx_passthrough(cin, midi0, midi1, midi2)
            
            # --- FCB Exp (Ch 5) ---
            elif channel == STOCK_CHANNEL - 1:
                if cc_num == 7: # Exp A -> HRP Vol
                    self.tx_translated(0xB0, HRP_CHANNEL - 1, 61, cc_val)
                elif cc_num == 27: # Exp B -> HRP Wah
                    self.tx_translated(0xB0, HRP_CHANNEL - 1, 62, cc_val)
                else:
                    self.tx_passthrough(cin, midi0, midi1, midi2)
            
            # --- ALL OTHER CCs ---
            else:
                self.tx_passthrough(cin, midi0, midi1, midi2)

        # 3. Everything Else (Clock, SysEx, etc.)
        else:
            self.tx_passthrough(cin, midi0, midi1, midi2)

# --- STARTUP ---
print("Pico 2 W Translator - Starting...")
# Use Blue for idle to distinguish from "Off/Red"
IDLE_COLOR = (0, 0, 20) # Very Dim Blue
pixel[0] = (255, 0, 0) # RED
pixel.write()
time.sleep(0.5)
pixel[0] = IDLE_COLOR
pixel.write()

translator = RigTranslator()
usb.device.get().init(translator, builtin_driver=(not STRICT_MIDI))

# Rotation animation helper # Removed
# angle = 0 # Removed

# Main loop - Cooldown only
while True:
    # is_open = usb.device.get().is_open() # Removed
    
    if pixel[0] != IDLE_COLOR:
        time.sleep_ms(100)
        pixel[0] = IDLE_COLOR
        pixel.write()
    # else: # Removed
        # Solid Dim Green if open, Pulsing BLUE/CYAN if waiting # Removed
        # if is_open: # Removed
            # pixel[0] = (0, 40, 0) # Brighter Dim Green # Removed
        # else: # Removed
            # Pulsing BLUE/CYAN to indicate waiting for host # Removed
            # pulse = int((math.sin(angle) + 1) * 32) # Removed
            # pixel[0] = (0, pulse, pulse) # Pulsing Cyan # Removed
        
        # pixel.write() # Removed
        # angle += 0.1 # Removed
        # if angle > 628: angle = 0 # Removed
    time.sleep_ms(10)
