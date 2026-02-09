<!-- @format -->

UnO firmware UnO2 firmware TinyBox

# banks 10 Up to 200 (theoretically \*) Up to 200

# presets 100 Up to 1000 (theoretically \*) Up to 1000

# messages/preset 8 Unlimited (theoretically \*) Unlimited

# MIDI channels 8 (global) 16 (for each message) 16 (for each message)

MIDI msg types PC, CC, Note All All

MIDI Clock - Start, Continue, Stop Start, Continue, Stop, Clock

Expr.pedal msg CC CC, AfterTouch, PitchBend CC, AfterTouch, PitchBend

Pedal sweep curve Linear Linear, FastRising, SlowRising

```
Linear, FastRising,
SlowRising
```

Bank layout possibilities

```
10 x 10 presets or
19 x 5 presets + 5
global stompboxes
```

```
Any mix of presets,
stompboxes, momentary
effects for each bank
```

```
Any mix of presets,
stompboxes, momentary
effects for each bank
```

Direct bank - + +

Programmable delay - + +

Use of data variables - + +

if..then...else logic - + +

Max. setup size 2048 bytes 2048 bytes 262144 bytes

Setlist support - - +

MIDI filter/router - - +

Built-in MIDI-USB itf - - +

Wireless status display - - (+ with Wino2 add-on) + (\*\*)

Phantom power - - +

```
(*) the total number of banks/presets/messages is limited by the 2048-byte setup memory of the
FCB1010. An online version of UnO2ControlCenter allows you to create a setup and inspect its size, in
order to verify if it fits in the UnO2 based solution, or if it requires the TinyBox hardware extension.
```

```
(**) the TinyBox requires a laptop running TinyBoxControlCenter to show the wireless status screen on
a tablet (or on the laptop itself), the Wino2 module doesn’t.
```

# Editor software for UnO/UnO2/Wino2/TinyBox

## FCB/UnO ControlCenter = editor for UnO / Wino firmware

FCB/UnO ControlCenter is a graphical editor to edit setups for an FCB1010
equipped with Behringer, UnO or Wino firmware. The latest Behringer version
(2.5) and all UnO / Wino versions are supported.

A license for this editor can be purchased at https://shop.fcb1010.eu/

The Wino kit allows to upload setups to the FCB1010 through WIFI instead of MIDI
SysEx.

## UnO2 ControlCenter = editor for UnO2 firmware

UnO2 ControlCenter is a text based editor to create setups for an FCB1010
equipped with UnO firmware. The text based approach is an essential element of
the UnO2 concept. The extended feature set makes a graphical approach
unsuitable. Therefore FCB/Uno ControlCenter cannot be used to program UnO2
setups.

Since the UnO2 firmware cannot be used without UnO2 ControlCenter, this editor
is included in the purchase of the UnO2 firmware.

The Wino2 kit installs a webserver inside the FCB1010. This server contains an
embedded version of UnO2 ControlCenter. Therefore the editor no longer needs to
be installed on a Windows or Mac computer.

## TinyBox ControlCenter = editor for the TinyBox hardware

The TinyBox comes with its own editor software included. It looks identical to
UnO2 ControlCenter but supports a larger command set to program the extended
TinyBox features.
