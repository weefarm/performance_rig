import usb.device
import time
from usb.device.midi import MIDIInterface

# Initialize the MIDI interface early so the host (mioXM) 
# sees it immediately upon power-up.
print("Waiting 2s for Thonny/Serial...")
time.sleep(2)

m = MIDIInterface()
usb.device.get().init(m, builtin_driver=True)
