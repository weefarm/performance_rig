import usb.device
from usb.device.midi import MIDIInterface

# Initialize the MIDI interface early so the host (mioXM) 
# sees it immediately upon power-up.
m = MIDIInterface()
usb.device.get().init(m, builtin_driver=True, product="Pico 2 MIDI Translator")
