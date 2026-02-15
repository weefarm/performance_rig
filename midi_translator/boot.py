# boot.py — USB MIDI device init BEFORE default CDC enumeration.
#
# Per MicroPython docs, placing usb.device init here ensures the
# board presents as a MIDI device on first enumeration, avoiding
# the disconnect/re-enumerate cycle that embedded USB hosts
# (like the mioXM) may not handle.
#
# The RigTranslator class is defined here so it's part of the
# initial USB descriptor set. main.py accesses it via the global.

import usb.device
from usb.device.midi import MIDIInterface

# USB-MIDI CIN constants
_CIN_PROGRAM_CHANGE = const(0x0C)


class RigTranslator(MIDIInterface):
    """MIDI translator: handles PC and CC remapping in on_midi_event."""

    # --- CONFIGURATION ---
    GCP_CH  = const(3)   # Channel 4 (0-indexed)
    FCB_CH  = const(4)   # Channel 5 (0-indexed)
    QC_CH   = const(0)   # Channel 1 (0-indexed)
    HRP_CH  = const(1)   # Channel 2 (0-indexed)

    def __init__(self):
        super().__init__()
        self.last_event_time = 0

    def on_midi_event(self, cin, midi0, midi1, midi2):
        import time
        self.last_event_time = time.ticks_ms()

        status = midi0 & 0xF0
        channel = midi0 & 0x0F

        if status == 0xC0:  # Program Change
            pc = midi1
            if channel == self.GCP_CH:
                if pc <= 7:
                    self.control_change(self.QC_CH, 35 + pc, 127)
                elif 8 <= pc <= 15:
                    self.control_change(self.QC_CH, 72 + pc, 127)
            elif channel == self.FCB_CH:
                if pc <= 7:
                    self.control_change(self.HRP_CH, 75 + pc, 127)
                elif pc == 8:
                    self.control_change(self.HRP_CH, 17, 127)
                elif pc == 9:
                    self.control_change(self.HRP_CH, 16, 127)
            else:
                self.send_event(_CIN_PROGRAM_CHANGE, 0xC0 | channel, pc, 0)

        elif status == 0xB0:  # Control Change
            cc, val = midi1, midi2
            if channel == self.GCP_CH:
                if cc == 1:
                    self.control_change(self.QC_CH, 1, val)
                elif cc == 2:
                    self.control_change(self.QC_CH, 2, val)
            elif channel == self.FCB_CH:
                if cc == 7:
                    self.control_change(self.HRP_CH, 61, val)
                elif cc == 27:
                    self.control_change(self.HRP_CH, 62, val)
            else:
                self.control_change(channel, cc, val)

        else:  # Everything else — passthrough
            try:
                self.send_event(cin, midi0, midi1, midi2)
            except:
                pass


# Create and register the translator BEFORE USB enumeration completes.
translator = RigTranslator()
usb.device.get().init(translator, builtin_driver=True)
