<!-- @format -->

(^) (^) (^) (^) (^) (^) (^) (^) (^)

# mio X-Series

(^)

## Advanced MIDI Interfaces

(^) (^) (^) (^) (^)

## User Guide

mio X-Series User Guide Version 20220503

Compliance Statement

```
mioXM meets the requirements of the following
standards and directives:
```

- FCC Part 15 Class B, Radiated Emissions
- CAN ICES-003 (B) / NMB-003 (B)
- CISPR 32 Class B
- EN 61000- 4 - 2
- EN 61000- 4 - 4

```
mioXL meets the requirements of the following
standards and directives:
```

- FCC Part 15 Class B, Radiated Emissions
- CAN ICES-003 (B) / NMB-003 (B)
- CISPR 32 Class B
- EN 61000 - 4 - 2
- EN 61000- 4 - 4

(^) Communication Statement This equipment has been tested and found to comply
with the limits for a Class B digital device, pursuant to part 15 of the FCC
Rules. These limits are designed to provide reasonable protection against
harmful interference in a residential installation. This equipment generates,
uses and can radiate radio frequency energy and, if not installed and used in
accordance with the instructions, may cause harmful interference to radio
communications. However, there is no guarantee that interference will not occur
in a particular installation. If this equipment does cause harmful interference
to radio or television reception, which can be determined by turning the
equipment off and on, the user is encouraged to try to correct the interference
by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which
  the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.

Changes or modifications not expressly approved by iConnectivity could void the
user’s authority to operate the equipment.

(^) Declaration of Conformity (mioXM) We iConnectivity declare that the mioXM
complies with Part 15 of the FCC Rules. Operation is subject to the following
two conditions: (1) this device may not cause harmful interference, and (2) this
device must accept any interference received, including interference that may
cause undesired operation. Declaration of Conformity (mioXL) We iConnectivity
declare that the mioXL complies with Part 15 of the FCC Rules. Operation is
subject to the following two conditions: (1) this device may not cause harmful
interference, and (2) this device must accept any interference received,
including interference that may cause undesired operation. (^) Disposal of Waste
Equipment by Users in the European Union This symbol on the product or its
packaging indicates that this product must not be disposed of with other waste.
Instead, it is your responsibility to dispose of your waste equipment by handing
it over to a designated collection point for the recycling of waste electrical
and electronic equipment. The separate collection and recycling of your waste
equipment at the time of disposal will help conserve natural resources and
ensure that it is recycled in a manner that protects human health and the
environment. For more information about where you can drop off your waste
equipment for recycling, please contact your local city recycling office or the
dealer from whom you purchased the product.

## Table of Contents

- mio X-Series User Guide Version
- Chapter 1: Introduction
    - What’s in the Box?
    - Minimum System Requirements
    - Warranty
- Chapter 2: Quick Start Guide
- Chapter 3: Modes of Operation
    - Power Off
    - Normal Mode
    - Bootloader Mode
- Chapter 4: mioXM Hardware Description
    - Front Panel
    - Rear Panel
- Chapter 5: mioXL Hardware Description
    - Front Panel
    - Rear Panel
    - mioXL User Interface
- Chapter 6: Using Presets
    - Preset Parameters
    - Global Parameters
    - Naming Presets
    - Naming Device Ports and RTP Sessions
- Chapter 7: Specifications
    - USB Host Port Power Delivery
    - Power Adapter
    - Dimensions and Weights
    - Other................................................................................................................................
- Appendix A: Software Installation
    - Full-Featured
      Operation...................................................................................................
    - Basic USB MIDI Interface Operation
- Appendix B: Using Bootloader Mode
    - Firmware File
      Format.......................................................................................................
- Appendix C: More Resources

## Chapter 1: Introduction

Congratulations on the purchase of your new mio X-Series interface!

Based on iConnectivity’s robust road-tested technology, the mio X-Series (a.k.a.
“mioX”) interfaces are the most advanced MIDI interfaces ever created, with
unrivalled configurability and network expandability.

mioXM

mioXL

iConnectivity makes every effort to develop simple and intuitive hardware and
companion control software. However, because your mioX interface includes so
many advanced features, we strongly recommend that you read this manual
carefully, even if you are an experienced MIDI user.

### What’s in the Box?

- mio X-Series Interface
- Universal Power Adapter: 100 V - 240 V AC, 50/60 Hz
- USB Cable: Type-A to Type-B
- Ethernet Network Cable
- Optional Rubber Feet (mioXL only, quantity 4)

### Minimum System Requirements

MacOS

- MacOS X 10.1 2 (Sierra)
- One free USB port or Ethernet port

Windows

- Microsoft Windows 10
- One free USB port or Ethernet port

### Warranty

The iConnectivity Warranty Policy may be found on our website at: Warranty
Policy

(^) (^) (^) (^) (^) For more information about these and other products, please
visit the iConnectivity Knowledge Base at the iConnectivity Support Website
Product Features, Specifications, and System Requirements may be subject to
change. Apple logo, macOS, OS X, and Mac are trademarks of Apple Inc.,
registered in the U.S. and other countries. iConnectivity, mio, mioX, mioXL, and
mioXM are trademarks of iKingdom Corp. © iKingdom Corp. 2022

## Chapter 2: Quick Start Guide

To start using your mioX interface as a standard USB-MIDI interface right away,
follow these steps:

1. MacOS Users: there are no software drivers to download or install; mioX
   interfaces use the USB MIDI class-compliant drivers built into MacOS. Windows
   Users: please download and install the latest version of our Unified Windows
   Driver from the iConnectivity web site Windows Drivers page.
2. Using the provided 12V power adapter, connect your mioX interface (power port
   located on the rear panel) to your power strip or wall outlet. Depending on
   your location, you may need to use one of the included international plug
   adapters.
3. Using the provided USB cable, connect your mioX to your computer (Type-B end
   to the cable to the mioX port marked USB-DAW, Type-A end to the computer). If
   your computer does not have USB Type-A ports, you will need to purchase an
   adapter.
4. Plug your MIDI instruments into the DIN-MIDI ports on your mioX interface.

These steps should get you up and running quickly. However, please note that you
will only be using a fraction of your mioX interface’s potential. In order to
unleash the full power of your mioX, we strongly recommend that you read this
entire user guide and install all of the recommended software. See Appendix A
(Software Installation) for more specific information.

## Chapter 3: Modes of Operation

mioX interfaces have three modes of operation:

1. Power Off
2. Normal Mode
3. Bootloader Mode

### Power Off

The mioX interface is powered off and not operational.

### Normal Mode

As you might guess, this is the normal operational mode that you will use nearly
all of the time. In this mode, the device is powered on and operates as a fully
functional interface.

### Bootloader Mode

Bootloader Mode is a special service mode used to perform firmware updates.
Normally you will use Auracle for X-Series software to update your firmware and
Auracle for X-Series will automatically switch your mioX between Normal and
Bootloader modes as necessary. In rare situations, mioX users may prefer to
manually update their firmware via the bootloader. This manual process is
described in detail in Appendix B (Using Bootloader Mode) of this guide.

## Chapter 4: mioXM Hardware Description

### Front Panel

(^) Function Button The Function Button on the front left of mioXM provides
several different functions:

- Powering On
- Powering Off
- Entering Bootloader Mode

Powering On

If the mioXM is currently in a Power Off state, quickly press and release the
Function Button to power up the interface into the Normal Mode of operation. On
start-up, mioXM will light the eight LEDs in a sequence of green then red
colors. When start-up is complete, only one of the four lower row LEDs will
remain illuminated; that indicates Normal Mode.

Powering Off

To power off the mioXM, press and hold the Function Button (for 4 to 5 seconds)
until all LEDs are turned off, then immediately release the button.

Entering Bootloader Mode

Bootloader Mode can only be manually entered from the Power Off state. First
verify that the mioX is powered off and then press and hold the Function Button
down. The unit will cycle through green LEDs then red. Once you see red LEDs,
release the button. Bootloader Mode is then indicated by alternately flashing
green DIN-MIDI and USB-MIDI LEDs.

Touch Panel

The interactive Touch Panel on the front of the mioXM controls several functions
of the interface and displays status on eight LEDs.

Top Row LEDs

The top row LEDs illuminate whenever there is activity on any of the I/O ports:

- USB-DAW (USB MIDI between mioX and your computer)
- RTP-MIDI (RTP/Network MIDI)
- DIN-MIDI (MIDI on DIN Ports)
- USB-MIDI (MIDI on USB Host Ports)

When the mioX transmits data to another device, the corresponding LED will light
up green. When the mioX receives data from another device, the corresponding LED
will light up red.

For example: If mioX receives USB MIDI from a connected computer, the USB-DAW
LED will light red. If mioX transmits MIDI out any of the DIN-MIDI ports, the
DIN-MIDI LED will light green.

Bottom Row Controls

The bottom row of the Touch Panel features four touch-sensitive controls, each
of which will load a memory preset (Mem 1 through Mem 4). When you touch the
area of a control, the mioX loads the appropriate memory preset and updates its
bottom row LEDs to indicate the currently active memory.

Note that only one Mem LED will light at a time. The LED color will usually be
green, indicating the preset is loaded and has not been edited by Auracle for
X-Series or other control software. If the current preset has been edited, the
LED will turn red; this is to remind you to save your work before loading
another preset. If you do save the preset, or load a new one, the appropriate
LED will turn green.

Front I/O Jacks

The front of the mioXM features several ports that communicate by various MIDI
protocols.

(^) If you are not already familiar with the MIDI protocols discussed here,
check out the iConnectivity Knowledge Base at: Intro to MIDI Connections

#### DIN 1 MIDI I/O

DIN 1 is a pair of ports (MIDI In and MIDI Out) on 5 - pin DIN connectors (where
‘1’ denotes the first pair of mioX DIN-MIDI ports). Connect these ports to other
devices with DIN-type MIDI connectors. Data flows into the mioX on a MIDI In
port and flows out from a MIDI Out port. Internally, the mioX routes MIDI data
between these and all other I/O ports, as configured by Auracle for X-Series
software.

RTP / Network MIDI

The RTP-MIDI port transmits and receives RTP/Network MIDI on a standard
ethernet-type connector. Use the provided ethernet cable to connect to an RTP
MIDI network (for example: your computer or another mioX). If you need a longer
run of ethernet cable, you can supply your own standard ethernet cable of
sufficient length. Internally, the mioX routes MIDI data between this and all
other I/O ports, as configured by Auracle for X-Series software.

The RTP-MIDI jack incorporates two useful LEDs:

- The yellow-orange LED lights to indicate the interface is connected to a
  functioning network. This LED will stay on continually while you are connected
  to the network.
- The green LED lights to indicate network traffic, i.e., it will flash each
  time an ethernet signal is sent or received via the RTP-MIDI port. Note that
  it is normal for this LED to flash occasionally while it is connected to a
  network, even if you are not currently sending MIDI at the time.

Device Port

The Device Port labelled USB-DAW is a standard USB Type-B connector. Using the
provided USB cable, connect your mioX to your computer (Type-B end of the cable
to the mioX USB-DAW port and the Type-A end to the computer). If your computer
does not have USB Type-A ports, you will need to purchase an adapter. Once
connected, the mioX will appear on your computer as a USB MIDI interface.

(^) Windows users must first download and install our Unified Windows Driver
from the iConnectivity web site Windows Drivers page. (^) Internally, the mioX
routes MIDI data between this and all other I/O ports, as configured by Auracle
for X-Series software.

### Rear Panel

(^) (^) Host Ports The 4 mioXM Host Ports “host” additional USB-MIDI devices
(for example: a keyboard controller). Internally, the mioX routes MIDI data
between these and all other I/O ports, as configured by Auracle for X-Series
software. Note that the Host Ports have no numbers written above or below them.
That is because host assignments are flexible: you can plug a USB-MIDI device
into any of these ports at any time. The first USB-MIDI device plugged in will
be assigned HST 1, the second device assigned HST 2, and so on. mioXM can even
host external (powered) USB hubs with additional USB-MIDI devices for a total
of 8. If you desire consistent host port numbering, Auracle for X-Series
software may be used to reserve port numbers for specific USB-MIDI devices in
your setup, regardless of what order your devices are plugged into the host
ports. (^) For more information on USB-MIDI Host port usage, peruse the
iConnectivity Knowledge Base at: mio X-Series Host Port (^) DIN-MIDI I/O Ports
In addition to the first DIN-MIDI I/O port (on the front of the device), there
are 3 additional pairs of DIN-MIDI I/O ports on the back of the mioX, each
carrying its own unique stream of MIDI data. Connect these ports to other
devices with DIN-type MIDI connectors. Similar to the DIN 1 port, data flows
into the device on a MIDI In connector and flows out from the device on a MIDI
Out connector. Internally, the mioX routes MIDI data between these and all other
I/O ports, as configured by Auracle for X-Series software.

Power Port

mioX requires power via its Power Port. Plug one end of the provided power
adapter into the device’s Power Port and the other end into your wall or power
strip outlet. Depending on your location, you may need to use one of the
included international plug adapters.

Always use the iConnectivity provided power supply. If you lose or damage yours,
we sell direct replacements. See the Specifications section of this guide for
details.

GND

Chassis GND is provided by a Phillips-head screw at the right end of the rear
panel. Although it is usually not necessary, depending on the location of your
mioX and your overall system configuration, you may need to connect the mioX
Chassis GND to other GND connections in your system. If you lose or damage your
GND screw, see the Specifications section of this guide for more details.

## Chapter 5: mioXL Hardware Description

### Front Panel

(^) Touch Panel The interactive Touch Panel on the front of the mioXL is an
integrated touch sensitive controller with two rows of status LEDs. The Touch
Panel, combined with the OLED Display and Parameter/Power Knob, control various
configuration parameters and modes of mioXL operation. For more information
refer to the mioXL User Interface section of this guide. OLED Display The mioXL
front panel features a high-resolution OLED (Organic Light Emitting Diode)
display. OLED is a modern display technology with a wider viewing angle, greater
contrast ratio, and quicker response time when compared to LCDs. The OLED
Display is a key component of the mioXL user interface and displays a variety of
data in the various mioXL menu screens. Parameter/Power Knob The Parameter/Power
Knob is a dual-purpose knob/pushbutton and performs various functions as it is
rotated and pressed. To make reading easier, we will refer to it as the
“Parameter Knob”, “Parameter Button”, or “Power Button”, depending on the
operation being performed. Its operation is detailed in the guide’s mioXL User
Interface section. Front I/O Jacks The mioXL front panel features several ports
that communicate by various MIDI protocols. (^) If you are not already familiar
with the MIDI protocols discussed in this guide, check out the iConnectivity
Knowledge Base at: Intro to MIDI Connections

DIN-MIDI I/O Ports

There are 8 DIN-MIDI I/O ports on the front of the mioXL, each carrying its own
unique stream of MIDI data. Connect these ports to other devices with DIN-type
MIDI connectors.

Data flows into the mioX on MIDI In ports and flows out from the mioX on MIDI
Out ports. The mioXL has a total of 8 DIN-MIDI inputs and 12 outputs. Therefore,
you will notice that DIN 7 and DIN 8 are MIDI I/O pairs and DIN 9, DIN 10, DIN
11, DIN 12 are MIDI output only.

Internally, the mioX routes MIDI data between these and all other I/O ports, as
configured by Auracle for X-Series software.

Host Ports

The 10 mioXL Host Ports (4 on the front, 6 on the rear) “host” additional
USB-MIDI devices (for example: a keyboard controller). Internally, the mioX
routes MIDI data between Host Ports and all other I/O ports, as configured by
Auracle for X-Series software.

Note that the Host Ports have no numbers associated with them. That is because
host assignments are flexible: you can plug a USB-MIDI device into any of these
ports at any time. The first USB-MIDI device plugged in will be assigned HST 1,
the second device assigned HST 2, and so on. If you desire consistent host port
numbering, Auracle for X-Series software may be used to reserve port numbers for
specific USB-MIDI devices in your setup, regardless of what order your devices
are plugged into the host ports.

(^) For more information on USB-MIDI Host port usage, peruse the iConnectivity
Knowledge Base at: mio X-Series Host Port (^) Device Port The Device Port,
labelled USB-DAW, is a standard USB Type-B connector. Using the provided USB
cable, connect your mioX to your computer (Type-B end of the cable to the mioX
USB-DAW port and the Type-A end to the computer). If your computer does not have
USB Type-A ports, you will need to purchase an adapter. Once connected, the mioX
will appear on your computer as a USB MIDI interface. (^) Before making this
connection, Windows users should first download and install our Unified Windows
Driver from our web site at: Windows Drivers (^) Internally, the mioX routes
MIDI data between this and all other I/O ports, as configured by Auracle for
X-Series software.

### Rear Panel

(^) (^) RTP / Network MIDI The RTP-MIDI port transmits and receives RTP/Network
MIDI on a standard ethernet-type connector. Use the provided ethernet cable to
connect to an RTP MIDI network (for example: your computer or another mioX). If
you need a longer run of cable, you can supply your own standard ethernet cable
of sufficient length. Internally, the mioX routes MIDI data between this and all
other I/O ports, as configured by Auracle for X-Series software. The RTP-MIDI
jack incorporates two useful LEDs:

- The yellow-orange LED lights to indicate the interface is connected to a
  functioning network. This LED will stay on continually while you are connected
  to the network.
- The green LED lights to indicate network traffic, i.e., it will flash each
  time an ethernet signal is sent or received via the RTP-MIDI port. Note that
  it is normal for this LED to flash occasionally while it is connected to a
  network, even if you are not currently sending MIDI at the time.

(^) Host Ports In addition to the 4 Host Ports on its front panel, mioXL has
another 6 Host Ports on its rear panel for “hosting” additional USB-MIDI
devices. Internally, the mioX routes MIDI data between these and all other I/O
ports, as configured by Auracle for X-Series software. For more info on Host
Ports, consult the mioXL front panel Host Ports section of this guide. DIN-MIDI
I/O Ports In addition to the DIN-MIDI I/O ports on the front of the device,
there are 6 more pairs of DIN-MIDI I/O ports on the back of the mioXL, each
carrying its own unique stream of MIDI data. Connect these ports to other
devices with DIN-type MIDI connectors. Once again, remember that data flows into
the device on a MIDI In connector and flows out from the device on a MIDI Out
connector.

Internally, the mioX routes MIDI data between these and all other I/O ports, as
configured by Auracle for X-Series software.

Power Port

mioX requires power via its Power Port. Plug one end of the provided power
adapter into the device’s Power Port and the other end into your wall or power
strip outlet. Depending on your location, you may need to use one of the
included international plug adapters.

Always use the iConnectivity provided power supply. If you lose or damage yours,
we sell direct replacements. See the Specifications section of this guide for
details.

GND

Chassis GND is provided by a Phillips-head screw at the right end of the rear
panel. Although it is usually not necessary, depending on the location of your
mioX and your overall system configuration, you may need to connect the mioX
Chassis GND to other GND connections in your system. If you lose or damage your
GND screw, see the Specifications section of this guide for more details.

### mioXL User Interface

The interactive Touch Panel on the front of the mioXL is an integrated touch
sensitive controller with two rows of status LEDs. The Touch Panel, combined
with the OLED Display and Parameter/Power Knob, are referred to collectively as
the User Interface (UI). The UI controls various configuration parameters and
modes of mioXL operation. This section will discuss the operation of the various
UI elements.

(^) Parameter/Power Knob The Parameter/Power Knob to the right of the display is
a dual-purpose knob/pushbutton and performs various functions as it is rotated
and pressed. To make reading easier, we will refer to it as the “Parameter
Knob”, “Parameter Button”, or “Power Button”, depending on the operation being
performed. One of the primary pushbutton functions is to set the current mioX
mode of operation:

- Powering On: If the mioXL is currently in a Power Off state, quickly press and
  release the Power Button to power up the interface into Normal Mode. On
  start-up, mioXL will light the LEDs in a sequence of green and red colors and
  then display its banner page (the product name and firmware version number)
  for a few seconds:

```
The display give way to the current memory preset number and preset name. The mioXL
is now in Normal Mode.
```

- Powering Off: To power off the mioXL, press and hold the Power Button (for 4
  to 5 seconds) until the OLED display and all LEDs are turned off, then
  immediately release the Power Button.
- Entering Bootloader Mode: Bootloader Mode can only be manually entered from
  the Power Off state. First verify that the mioX is powered off and then press
  and hold the Power Button down (for 4 to 5 seconds) as the unit cycles the
  eight LEDs through green then red colors. After all LEDs are off, immediately
  release the Power Button. Bootloader Mode is then indicated by a blank display
  and alternately flashing green DIN-MIDI and USB-MIDI LEDs.

Top Row Controls

The four top row LEDs of the Touch Panel illuminate whenever there is activity
on each type of I/O port:

- USB-DAW (USB MIDI between mioX and your computer)
- RTP-MIDI (RTP/Network MIDI)
- DIN-MIDI (MIDI on DIN Ports)
- USB-MIDI (MIDI on USB Host Ports)

When the mioX transmits data to another device, the corresponding LED will light
up green. When the mioX receives data from another device, the corresponding LED
will light up red.

For example: When mioX receives USB MIDI from a connected computer, the USB-DAW
LED will light red. When mioX transmits MIDI data out any of the DIN-MIDI ports,
the DIN-MIDI LED will light green.

The top row LEDs are also touch-sensitive controls that select screens for
monitoring MIDI activity. Each type of port has a page that displays activity on
all ports simultaneously. All MIDI monitor pages appear and operate in a similar
fashion; take DIN-MIDI for example:

The upper line of dots indicates activity on DIN In ports 1 through 8. The lower
line of dots indicates DIN Out ports 1 through 12. In this example, the two
brighter dots indicate DIN-MIDI activity present on IN 2 and OUT 3.

While monitoring MIDI activity, you may quickly switch pages by turning the
Parameter Knob clockwise or counterclockwise. You may also exit a MIDI
monitoring page by pressing any bottom row control.

Bottom Row Controls

The bottom row LEDs are touch-sensitive controls that affect preset operation:

- The Back control decrements the Preset number and wraps from Preset 1 to
  Preset 32.
- The Next control increments the Preset number and wraps from Preset 32 to
  Preset 1.
- The Load control selects a Preset Memory and makes it active.
- The Save control saves a copy of the current preset to a Preset Memory.

(^) Preset Manipulation The mioXL stores up to 32 presets in Preset Memory.
There are three primary methods for manipulating presets:

1. Use the front panel bottom row controls
2. Use the Parameter Knob
3. Use Auracle for X-Series software

(^) (^) To learn more about Auracle for X-Series software, please visit the
iConnectivity web site at: Auracle for X-Series (^) (^) We will describe the
first two methods here. Pressing a Back or Next control, or rotating the
Parameter Knob, will increment or decrement your way through all of the preset
memory locations, allowing you to preview presets before committing to load or
save them. Remember: Previewing is a temporary action; it does not automatically
change presets. Loading a Preset To load a new preset, preview your way to the
desired preset memory location and either press the Load control or the
Parameter Button.

Saving a Preset

To save the current preset back to the current preset memory location, simply
press the Save control.

To save the current preset to another preset memory location, preview your way
to the desired destination preset memory location via the Back or Next controls
(or by rotating the Parameter Knob) and then press the Save control.

**“** Edited **Preset” Indication**

If the current preset has been edited (by Auracle for X-Series or other control
software), the mioXL will display a diamond character to the left of the preset
name:

This is to remind you to save your work before loading another preset. Once you
save the preset, or deliberately load a new one, the diamond will disappear.

## Chapter 6: Using Presets

mio X-Series devices store various elements of your setup internally. The stored
parameters are classified as preset memory (“Preset”) parameters or Global
parameters.

### Preset Parameters

Presets are the setup memories (4 on mioXM and 32 on mioXL) that may be stored
and recalled by the user at any time. The following parameters are saved as a
Preset:

- Preset Name
- MIDI Routing
- MIDI Filters
- MIDI Channel Remapping

### Global Parameters

Global parameters are those that apply regardless of what preset is loaded. In
other words, elements of your global setup are used across all presets. In
addition, when you edit global parameters from Auracle for X-Series software,
they are stored immediately to the mioX device. The following are global
parameters:

- Port Names
- USB Host Port Reservations
- RTP / Network MIDI Setup

### Naming Presets

mioX preset names must comply with the following rules:

1. The minimum name length is 1 character
2. The maximum name length is 15 characters
3. The name allows the use of all printable ASCII characters

### Naming Device Ports and RTP Sessions

Device Port and RTP Session naming is a little more restrictive than preset
naming. The following rules apply to Device Ports and RTP Sessions:

1. The minimum name length is 2 characters
2. The maximum length is 15 characters
3. The first character of the name must be a letter (upper or lower case)
4. The name must be made up of allowable characters only: upper case letters 'A'
   to 'Z' lower case letters 'a' to 'z' numbers '0' to '9' ' ' space '\_'
   underscore '.' period ',' comma '-' minus '+' plus '/' forward slash '('
   curve bracket left ')' curve bracket right '<' angle bracket left '>' angle
   bracket right '[' square bracket left ']' square bracket right '{' curly
   bracket left '}' curly bracket right

## Chapter 7: Specifications

### USB Host Port Power Delivery

```
Max Current (per port) Total Current (per unit)
mioXM 500 mA 2000 mA (2A)
mioXL 500 mA 3000 mA (3A)
```

### Power Adapter

```
Output +12V DC, 3A (36W)
Input 100V - 240V AC, 50/60 Hz
Plug Center pin positive
2.5 mm inside diameter
5.5 mm outside diameter
12 mm length
Model # iConnectivity iCP4
```

### Dimensions and Weights

```
mioXM mioXL
Height 1U: 1.48” (37.5 mm) 1U: 1.75” (44.5 mm)
Width 8.43” (214 mm) 19” (483 mm)
Depth 5.51” (140 mm) 4.72” (120 mm)
Weight 2.18 lbs (989 g) 4.02 lbs (1825 g)
```

### Other................................................................................................................................

```
GND Screw M3 x 0.5 x 6 mm, pan head, Phillips, black zinc
```

## Appendix A: Software Installation

Software should be installed on your computer before using your mioX device.
Complete full- featured mioX operation relies on three different software
components:

- Software (USB MIDI) device drivers
- RTP/Network MIDI support
- Auracle for X-Series configuration software

### Full-Featured Operation...................................................................................................

MacOS Users

MacOS full-featured installs are easy. The first two components are built into
MacOS! The third component, Auracle for X-Series software, must be downloaded
from the iConnectivity web site Auracle for X-Series page and installed on your
computer. Be sure to download the MacOS version specifically.

Windows Users

For full-featured Windows use, none of the three components are built-in;
however, the installation is still easy. Merely download the Windows version of
Auracle for X-Series software from the iConnectivity web site Auracle for
X-Series page and run the installer. The Auracle for X-Series installer will
install all three components onto your computer.

### Basic USB MIDI Interface Operation

In order to unleash the full power of your mioX (including but not limited to
firmware updates, MIDI routing and filtering, and RTP/Network MIDI), we strongly
recommend that you install all three software components listed above. However,
some users may want to run their mioX as a simple USB MIDI interface with no
advanced functionality.

MacOS Users

For basic USB MIDI interface operation, MacOS users merely connect the mioX
device to their computer’s USB port and start playing.

Windows Users

For basic USB MIDI interface operation, Windows users download and install the
latest version of our Unified Windows Driver from the iConnectivity web site
Windows Drivers page.

## Appendix B: Using Bootloader Mode

Bootloader Mode is a special service mode used to perform firmware updates. It
may be entered automatically (via iConnectivity software Auracle for X-Series,
Auracle, and iConfig) or manually (via a specific sequence of manual steps).

The preferred method for updating your device’s firmware is to use iConnectivity
software. Our software can check if newer firmware is available and if so,
download it into your device. The software method is automated and switches your
device modes for you.

In rare situations, you may prefer to manually update your firmware using the
bootloader. This will require several steps:

1. Download the firmware from the iConnectivity website Firmware Page
2. Manually set your mioX interface to Bootloader Mode: [mioXM] [mioXL]
3. Transmit the firmware file to the mioX interface and allow the update to
   complete
4. Manually restart your mioX by first powering off the device: [mioXM] [mioXL]
   and then powering on again: [mioXM] [mioXL]

### Firmware File Format.......................................................................................................

iConnectivity firmware is formatted as a Standard MIDI File with a .MID file
extension. That means that standard MIDI software such as DAWs, Standard MIDI
File Players, and System Exclusive (a.k.a. “SysEx”) applications can be used to
transmit the firmware data to your interface.

Examples of software that we have tested and can recommend are:

- Snoise SysEx Librarian
- Sweet MIDI Player
- MIDI-OX

(^) For more details on using standard MIDI software to manually update your
firmware, please see this Knowledge Base article.

## Appendix C: More Resources

The iConnectivity website and iConnectivity Knowledge Base contain a wealth of
helpful written articles and tutorials, as well as instructional videos.

For your convenience, selected hyperlinks into these systems are listed below:

The iConnectivity Knowledge Base main page is located at: iConnectivity Support
Website.

Download our latest Unified Windows Driver from the website Windows Drivers
page.

Download Auracle for X-Series software from the website Auracle for X-Series
page.

Video Guides on configuring your system using Auracle for X-Series software.

Download the latest firmware from the website Firmware page.

MIDI protocols are explained on our Knowledge Base Intro to MIDI Connections
page.

USB-MIDI Host Port usage is described on our Knowledge Base mio X-Series Host
Port page.

The Factory Reset procedure is described at the Knowledge Base mioX Factory
Reset page.
