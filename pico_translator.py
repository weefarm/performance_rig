import machine
import time
import neopixel
import usb.device
from usb.device.midi import MIDIInterface
from machine import I2C, Pin

# --- CONFIGURATION ---
NUM_LEDS = 9        # 8 outer ring + 1 center
NEO_PIN  = 15       # GPIO for WS2812 Data
I2C_SDA  = 4        # GPIO for OLED SDA
I2C_SCL  = 5        # GPIO for OLED SCL

GCP_CHANNEL   = 4   # Incoming Channel for Ground Control Pro
STOCK_CHANNEL = 5   # Incoming Channel for Stock FCB1010

QC_CHANNEL    = 1    # Outgoing Channel for Quad Cortex
HRP_CHANNEL   = 2    # Outgoing Channel for HeadRush Prime
MC_CHANNEL    = 3    # Outgoing Channel for Microcosm

# --- INITIALIZATION ---
pixels = neopixel.NeoPixel(Pin(NEO_PIN), NUM_LEDS)
i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL))

# OLED Init
try:
    import ssd1306
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
except ImportError:
    display = None
    print("OLED: ssd1306.py not found")

# --- FEEDBACK HELPERS ---
def set_leds(center_color, ring_color=None, ring_index=None):
    # Center LED
    pixels[8] = center_color
    # Optional single Ring LED (Tally)
    if ring_index is not None and ring_color:
        for i in range(8):
            pixels[i] = (0,0,0) # Clear others
        pixels[ring_index] = ring_color
    pixels.write()

def update_display(line1, line2="", line3=""):
    if display:
        display.fill(0)
        display.text("MIDI TRANSLATOR", 0, 0)
        display.text("-" * 15, 0, 10)
        display.text(line1, 0, 25)
        display.text(line2, 0, 40)
        display.text(line3, 0, 55)
        display.show()

# --- TRANSLATOR LOGIC ---
class RigTranslator(MIDIInterface):
    def on_program_change(self, channel, number):
        # Activity pulse
        set_leds((0, 255, 0), (0, 255, 0), channel) # Green center + Channel index
        
        # 1. GCP (Ch 4) -> QC (Ch 1)
        if channel == GCP_CHANNEL - 1: # 0-indexed
            if number <= 7: # PC 0-7 -> CC 35-42 (Stomps)
                cc_num = 35 + number
                self.control_change(QC_CHANNEL - 1, cc_num, 127)
                update_display("GCP -> QC", f"STOMP: {chr(65+number)}", f"CC {cc_num}")
            elif number >= 8 and number <= 15: # PC 8-15 -> CC 80-87 (Scenes)
                cc_num = 72 + number
                self.control_change(QC_CHANNEL - 1, cc_num, 127)
                update_display("GCP -> QC", f"SCENE: {chr(65+(number-8))}", f"CC {cc_num}")
                
        # 2. Stock FCB (Ch 5) -> HRP (Ch 2)
        elif channel == STOCK_CHANNEL - 1:
            if number <= 7: # PC 0-7 -> CC 75-82 (Toggles)
                cc_num = 75 + number
                self.control_change(HRP_CHANNEL - 1, cc_num, 127)
                update_display("FCB -> HRP", f"TOGGLE: {number+1}", f"CC {cc_num}")
            elif number == 8: # PC 8 -> HRP Prev Rig
                self.control_change(HRP_CHANNEL - 1, 17, 127)
                update_display("FCB -> HRP", "PREV RIG", "CC 17")
            elif number == 9: # PC 9 -> HRP Next Rig
                self.control_change(HRP_CHANNEL - 1, 16, 127)
                update_display("FCB -> HRP", "NEXT RIG", "CC 16")
        
        # Pass through others
        else:
            self.send_program_change(channel, number)

    def on_control_change(self, channel, controller, value):
        # 1. GCP Exp Pedals (Ch 4)
        if channel == GCP_CHANNEL - 1:
            if controller == 1: # Wah
                self.control_change(QC_CHANNEL - 1, 1, value)
            elif controller == 2: # Vol
                self.control_change(QC_CHANNEL - 1, 2, value)
                
        # 2. Stock FCB Exp Pedals (Ch 5)
        elif channel == STOCK_CHANNEL - 1:
            if controller == 7: # Exp A
                self.control_change(HRP_CHANNEL - 1, 61, value)
            elif controller == 27: # Exp B
                self.control_change(HRP_CHANNEL - 1, 62, value)
        
        # Pass through
        else:
            self.send_control_change(channel, controller, value)

# --- STARTUP ---
translator = RigTranslator()
usb.device.get().init(translator, builtin_driver=True, product="Pico 2 MIDI Translator")

print("Pico 2 W Translator Active...")
update_display("STATE: READY", "HUB: mioXM")
set_leds((0, 0, 255)) # Blue center = Healthy
