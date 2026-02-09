<!-- @format -->

# Wino2 user manual

## Contents

Document versions

Version 2.0 27/09/2025 Adapted to Wino2 v.2 = optional add-on to UnO2 v2
firmware

- Introduction: what is Wino2?
- IMPORTANT prerequisite :
- The Wino2 module
- Getting started
    -   1.  Open up the
            FCB1010.................................................................................................................
    -   2.  If not done already : install the UnO2 chip
    -   3.  Install the Wino2 WIFI module
    -   4.  Initialize the firmware for use with the Wino2 module
    -   5.  Calibrate the expression pedals
    -   6.  Connect to the FCB1010 through WIFI
    -   7.  Open the embedded web application
    -   8.  Register the UnO2 firmware (if not already done)
    - IMPORTANT REMARK about UnO2 ControlCenter
- The Wino2 web application
- Global configuration
    -   1.  Changing the embedded access point SSID or
            password.........................................................
    - Connecting to the FCB1010 using your home WIFI access point
    -   2.  Sending MIDI over WIFI
    -   3.  Enabling MIDI THRU
- Saving and sending FCB1010 setups
    -   1.  Saving the setup source
    -   2.  Sending the setup binary
- SysEx checksum calculator
- MIDI monitor screen
    - Message filtering
- APPENDIX: Factory reset, self-test and pedal calibration

## Introduction: what is Wino2?

In short : Wino2 is the acronym for “WIFI-enabled UnO2”

Some time ago we created the UnO2 firmware, which was not an extension of the
UnO firmware, but rather a spin-off of the TinyBox hardware (
https://www.tinybox.rocks/ ). Instead of the rigid 10x preset stucture, with up
to 8 messages per preset, a TinyBox setup can contain any number of “presets”,
“stompboxes” or “triggers”, organized in a fully flexible bank structure, and
each preset can contain any number of MIDI messages, sent on any of the 16 MIDI
channels. UnO2 firmware took that same approach, be it without the extended
setup memory space of the TinyBox hardware.

Now we decided to bring some more TinyBox functionality to the UnO2 equipped
FCB1010. By installing the Wino2 module inside the FCB1010, you can make the
floorboard WIFI enabled. This allows you to wirelessly connect your laptop or
iPad to the FCB1010 and view live status info of your MIDI controller using the
browser: current bank, selected preset, activated effects, etc.

The built-in webserver also hosts an identical copy of the UnO2 ControlCenter
editor software, which you can use to store and compile your UnO2 setup directly
on the FCB1010. Making the FCB1010 WIFI enabled finally removes one of the big
hurdles in programming the FCB1010: no more need for a MIDI- USB interface to
connect the FCB1010 to your laptop. Many cheap interfaces unfortunately turn out
to be incompatible with the FCB1010. So far the only solution was to purchase a
more expensive MIDI- USB interface with dedicated drivers and large enough data
buffers. The Wino2 module eliminates that requirement – instead of spending your
money on a compatible MIDI-USB interface you can purchase a Wino2 module which
offers the interesting extra functionality of a live status display and more.

Being WIFI enabled allowed to add a nice extra feature: you can send or receive
MIDI to or from your laptop or iPad over WIFI, using a protocol called “RTP
MIDI” or “AppleMIDI”.

Read on to learn all details about Wino2.

## IMPORTANT prerequisite :

Please be aware that the Wino2 module requires the use of UnO2 v.2.0 (or higher)
firmware. Earlier versions don’t contain the necessary communication with the
Wino2 module to report switch presses or effect activations. Wino2 needs that
info to be able to show a live status screen.

( this remark only concerns the current “version 2” Wino2 module, released
September 2025. The initial “version 1” Wino2 module was delivered with its own
dedicated Wino2 firmware, and is not compatible with UnO2 firmware )

## The Wino2 module

The wireless connection provided by this module replaces the 2-way MIDI
connection required so far to program the FCB1010. Moreover this module also
contains the UnO2ControlCenter application, adapted to run in a browser window.
No more need for any software installation to program your floorboard.

```
Installing the module is very simple. No soldering required, all you need is a screwdriver!
```

## Getting started

### 1. Open up the FCB1010.................................................................................................................

Turn the FCB1010 upside down, remove 16 screws to open the housing, lay the
bottom plate next to the housing (leave the ground wire connected)

### 2. If not done already : install the UnO2 chip

Remove the original firmware chip from the socket on the main board. If
necessary remove all hot melt adhesive which might be applied to the chip. You
can use a small screwdriver to lift the chip out of the socket without bending
the chip legs.

Store the original chip in a safe place, you might want to have it available if
you would ever sell your FCB1010.

Before inserting the UnO2 chip, make sure the chip legs are perfectly
perpendicular to the chip body. You can do that by slightly rotating the chip on
a flat surface as follows :

Place the UnO2 chip in the socket using the same orientation: the notch on one
side of the EPROM must match the notch on the EPROM socket. Be careful not to
press too hard, and pay attention not to bend any of the EPROM pins during
insertion.

### 3. Install the Wino2 WIFI module

On the FCB1010 main board, unplug the red/black wire unit with 4 leads, which is
running from the small MIDI connector board to the main board. Before you can do
so it may be necessary to (carefully!) remove applied hot melt adhesive. Never
pull the wires, you might pull them out of the connector housing. Instead remove
all hot glue and wiggle the connector itself until it loosens from the main
board.

Remove following 2 screws which hold the FCB1010 switch board :

Reuse the 2 screws to mount the WIFI module. The module orientation is so that
the 4-pins connector is close to the now empty 4-pins connector on the FCB1010
main board. Plug the large red/black wire into the connector of the WIFI module,
and plug the short wire unit of the WIFI module into the 4-pins connector of the
main board :

The FCB1010 inside now looks like this :

Before closing the FCB1010 housing again using the 16 screws, you can check if
the modification was done correctly. Power up the FCB1010, the display should
show “-lic” if the UnO2 firmware was just installed. If you have been using the
UnO2 firmware already, the display will show the same startup sequence as
before: “---” for a short time, followed by the bank number (“01” if a setup is
loaded, “00” in case of an empty setup)

If “-lic” is displayed, the UnO2 firmware still needs to be registered. This is
done in a later step of this

### tutorial.

### 4. Initialize the firmware for use with the Wino2 module

Now you can activate the communication between UnO2 firmware chip and Wino2 WIFI
module by power cycling the floorboard and keeping switches 1 and 9 pressed
during power up. The activated “Wino2 mode” is indicated by a row of green LEDs
lighting up on the FCB1010:

Whenever you would decide to remove the Wino2 module, you can do the same 1+9
footswitch click during startup to disable the communication again. Not doing so
would result in several SysEx status messages being sent to the MIDI OUT
connector of the FCB1010 on each switch click. Those messages are filtered out
by the Wino2 module when it is installed.

### 5. Calibrate the expression pedals

If not done already, don’t forget to calibrate the FCB1010 expression pedals.
Failing to do so is the most common cause for non-working expression pedals.
Calibration instructions can be found in the Behringer manual or by googling
“FCB1010 calibration”. Keeping the 1+3 switches pressed during power-up
initiates the calibration procedure. Keeping the 1+5 switches pressed during
power-up initiates a full test procedure of all FCB1010 hardware components,
followed by the pedal calibration.

### 6. Connect to the FCB1010 through WIFI

Use your laptop or iPad to connect to the WIFI access point which is now
embedded in the FCB1010. The SSID “FCB1010” should appear in your list of
available WIFI networks (sample screenshots taken from a Windows computer) :

Select the access point with SSID FCB1010 , and fill in the password, which is
FCB_Wino

Remark :

Further on in this manual you will learn an alternative way of connecting to the
FCB1010, using your home router instead of the embedded access point. That has
the advantage of retaining your internet connection while being connected to the
FCB1010. As you can see in the screenshot above no internet is available while
using the embedded Wino2 access point.

### 7. Open the embedded web application

With your laptop wirelessly connected to the FCB1010 access point, you can open
the embedded web application by surfing to IP address 192.168.4.1. Preferably
use Google Chrome (or a recent MS Edge browser on Windows), although Safari also
works correctly on MacOS.

If at first you see some weird, scrambled web page, don’t worry. Press the
Refresh button or close the browser tab and open a new one. The embedded WIFI
access point is not as strong as a dedicated router, so the initial page loading
can take some time or require a refresh to get all script and stylesheet files
downloaded. After the initial page load, things will run much smoother since the
browser caches the downloaded files, and status updates or setup edits no longer
require any extra file downloads.

### 8. Register the UnO2 firmware (if not already done)

If you have been using the UnO2 firmware before, you are ready to go. If not,
the FCB1010 display shows “-lic” and you first need to register the UnO2
firmware.

Click the icon which opens the full user interface (more details about this
later)

Now click the padlock icon in the editor menu bar:

This opens the registration form where you can fill in the data which you
received through email when placing the UnO2 order. The info is also printed on
the cardboard box which contained the UnO firmware chip.

Attention:

- Copy-and-paste the data exactly as received, all 3 fields are case sensitive
- Make sure you run the web browser on an internet connected device, so that the
  application can connect to the online license server.
- Initial connection to the license server may give a timeout error. In that
  case, just click the Register button again.

If you can’t combine a wired Ethernet connection (for internet access) with the
FCB1010 WIFI connection, you can also connect the Wino2 module to your home
router, instead of connecting directly to the FCB1010 using its internal access
point. More info about this a bit further in this manual, in the chapter
“Connecting to the FCB1010 using your home WIFI access point”

Of course, you can also choose to register the firmware using UnO2 ControlCenter
installed on your PC. This procedure is described in the UnO2 user manual.

That’s it, now you are ready to rock and roll!

Detailed info about the embedded UnO2 ControlCenter (which is identical to the
version installed on a Windows or Mac PC) and the “programming language” used
for creating your FCB1010 setup can be found in the UnO2 user manual.

### IMPORTANT REMARK about UnO2 ControlCenter

With the Wino2 module installed, it is important to stick to using the embedded
editor and not the PC editor for programming the Wino2 equipped FCB1010. This is
necessary because the embedded editor not only sends the compiled setup binary
to the FCB1010 main board, but it also stores setup info on the Wino2 module
itself. The module uses this info to show live status info (including bank,
preset and effect names) in the browser. The compiled setup binary created by
the PC editor doesn’t contain this info. Therefore, mixing the use of the PC
editor and the embedded editor may result in status info not being correctly
displayed.

More details about this can be found in the chapter “Saving and sending FCB1010
setups”.

If you have programmed the UnO2-equipped FCB1010 prior to installing the Wino2
module, simply copy-and-paste your earlier text-based setup from the PC editor
to the browser-based application, and

## continue using this last one from now on.

## The Wino2 web application

The web page shown when browsing to the FCB1010 IP address has 4 large icons in
its header bar. These serve to choose the preferred combination of application
views :

```
The first one, opened by default, is the FCB1010 status page. It shows an image of the
FCB1010, with info on the currently selected bank, which presets are assigned to which
switch, which effects are activated, etc. This is also a remote control for your FCB1010!
```

```
The next one shows a combination of all available windows on 1 screen :
```

- a shrinked status page
- an editor window containing your setup code
- a MIDI monitor window which shows all MIDI sent by the FCB This screen can be
  useful while testing out setup changes

This icon selects a combination of editor window and MIDI monitor, again useful
while testing setup changes. Collapsing the status page leaves more space for
the editor and monitor windows

Use the full-screen editor page while creating your setup.

```
The icon to the left of the 4 display option buttons toggles the browser window
between “fullscreen” and normal mode. Fullscreen mode will mainly be interesting
for displaying the status screen during a gig, since you won’t be using your iPad or
laptop for anything else at that moment.
```

## Global configuration

A few global configuration settings can be configured by clicking the cog icon
at the right side of the header bar:

### 1. Changing the embedded access point SSID or password.........................................................

The first tab of the configuration screen lets you modify the IP address of the
Wino2 module (actually there is little reason to do so, but you can...) or the
SSID and password of the Wino2 access point.

Attention : the password needs to be 8 characters minimum!

These settings can be reset at all time (for instance in case you would forget
the modified password) by keeping the FCB1010 1+2 footswitches pressed during
power-up. This reverts all access point settings to its defaults, which are :

```
IP : 192.168.4.
SSID : FCB
Password : FCB_Wino
```

### Connecting to the FCB1010 using your home WIFI access point

The Wino2 module has an interesting extra WIFI option: next to the built-in
access point, which we used so far, you can also let the Wino2 module connect to
your regular WIFI access point at home. This way both your FCB1010 and your
laptop can connect to the same access point, and you can reach the FCB1010 by
surfing to its newly assigned IP address (see below). The major advantage of
this is that your laptop doesn’t lose its internet connectivity this way
(provided that your WIFI access point is connected to the internet through your
home router of course)

While currently still connected to the Wino2 embedded access point, click the
second tab of the global settings menu, labeled “Network 2” :

Click the “Scan” button to search for nearby WIFI access points :

#### :

Then click the “Connect” button of the preferred access point, and (if required)
enter its password :

When connection succeeds, the access point will supply an IP address to the
FCB1010. It is mentioned in the setup menu :

With this configuration now stored in the Wino2 module, you can disconnect your
laptop from the Wino2 embedded access point, and connect to your regular home
access point again. Now open your browser, and instead of entering the default
Wino2 IP address 192.168.4.1, enter the IP address which was mentioned in the
setup menu above. Your laptop will again connect wirelessly to the FCB1010,
while maintaining its internet connection through your home router.

Pay attention to the modified IP address typed in the browser address bar in
screenshot below:

For creating or editing your Wino2 setup, you will prefer to use this new WIFI
configuration. It allows you to reach your FCB1010 by surfing to its assigned IP
address, without changing any of your original laptop WIFI settings. On the
other hand, while at a gig, you can have a live status view of your FCB by
connecting your iPad to the embedded Wino2 access point and surfing to
192.168.4.1. Indeed, you would not want to rely on any public access point for
viewing status info during a gig.

Both connection methods (through embedded access point or via an external access
point) remain simultaneously available, so after returning from a gig you can
again connect through your home router without any reconfiguration required.

### 2. Sending MIDI over WIFI

Having WIFI connectivity available allows us to let the FCB1010 send wireless
MIDI to a laptop, or receive wireless MIDI from a laptop and forward it to other
MIDI devices through its MIDI OUT connector. No more need for an extra “WIDI”
dongle!

The Wino2 module uses the “RTP-MIDI” technology for this. More info about this
MIDI standard can be found on following links :

- https://www.midi.org/midi-articles/rtp-midi-or-midi-over-networks
- https://en.wikipedia.org/wiki/RTP-MIDI

On macOS and iOS, RTP-MIDI (also known as AppleMIDI) is supported out of the
box.

On Windows, a free RTP-MIDI driver can be installed. More info about that in the
links above.

On Android, an app called MIDI Connector adds support for the RTP-MIDI protocol.

You can enable RTP-MIDI in the “MIDI routing” tab of the setup menu :

### 3. Enabling MIDI THRU

The same “MIDI routing” tab above also has a checkbox to enable MIDI THRU. When
doing so, all MIDI sent to the FCB1010 through its MIDI IN connector will be
forwarded to the MIDI OUT connector.

## Saving and sending FCB1010 setups

Without going into detail about how to program the Wino2 equipped FCB1010 setup
(this is covered in great detail in the UnO2 user manual) let’s continue going
through all menu options of the web application. Next to the cog icon discussed
above, the editor window also has a Save button and a Send button

### 1. Saving the setup source

The Save button stores the setup text, which you have entered in the editor
window, in the non-volatile memory of the Wino2 module. Click the Save button
regularly in order not to lose your work while creating your setup.

As you will notice, the Wino2 module can store one single setup source file.
However, thanks to the fact that this “setup source” is actually plain text, it
is very easy to copy-and-paste the full setup text from the browser into any
text editor and save the setup on your laptop, and vice versa load one of
multiple alternative setups, stored on your laptop, into the web application and
save it on the Wino2 module.

By the way, it is definitely a good idea to make an extra copy of your setup
source text on your laptop this way. In case a hickup would occur when saving
the setup to the Wino2 storage space, you then still have a backup of the setup
source on your laptop.

### 2. Sending the setup binary

In order for your setup to be used by the FCB1010, it is first “compiled” into
binary data. When clicking the “Send” button this binary data is sent from the
Wino2 module to the FCB1010 main board, where it is stored in the permanent
setup memory (the same memory which stores a Behringer, UnO or UnO2 setup when
no Wino2 module is installed)

For those who really like to know every little detail of the system: If you look
closely at the popup shown after clicking the Send button, you will notice 2
different status messages: first it says “Saving setup structure”, followed by
“Storing setup...”. Indeed, before storing the binary setup data in the FCB1010
setup memory, the setup structure (bank names, bank layout, switch assignments,
... ) is retrieved from the setup source text, and stored separately on the
Wino2 module. During a gig this info is combined with live data sent from the
FCB1010 main board to the Wino2 module to show extended status info in the
browser.

## SysEx checksum calculator

Just as a small convenience tool, we added a SysEx checksum calculator. Some
devices can be controlled through proprietary SysEx messages, and those messages
sometimes require a checksum being added as last byte of the message (mainly the
case for Roland devices). The included checksum calculator was created by
shingo45endo and is available on github :

https://github.com/shingo45endo/sysex-checksum

## MIDI monitor screen

Things are not always working correctly right from the start. If your gear
doesn’t behave as expected you might want to inspect the MIDI messages which the
FCB1010 sends. You can do so with the monitor screen of the built-in web
application. With this monitor you can get a detailed inside view on all
outgoing MIDI traffic.

The MIDI message list shown in that screen contains following data for each
transmitted MIDI message:

## - Timestamp on which the message was received or sent

- Hexadecimal representation of the MIDI message. A MIDI message can contain 1,
  2 or 3 bytes, except for SysEx messages which can contain more bytes and are
  shown on multiple lines in

## the message list

## - Text representation of the MIDI message, which is :

## o The MIDI channel (between 01 and 16), where applicable

## o The MIDI message type

## o 0, 1 or 2 MIDI data bytes (or multiple bytes in case of SysEx)

Attention: be aware that showing a lot of MIDI info in the browser can slow down
the transmission of MIDI by the Wino2 module. Therefore, use the monitor screen
only while inspecting or troubleshooting your setup, never during live use of
the FCB1010.

### Message filtering

The amount of MIDI data sent by the FCB1010 can be large, especially when using
the expression pedals. Therefore, the monitor screen has the option to filter
out certain message types, typically sent when using the expression pedals. For
ControlChange messages you can choose which CC number is being filtered (e.g.
CC07 & CC04, which are continuous control messages)

## APPENDIX: Factory reset, self-test and pedal calibration

The UnO2 firmware contains the same self-test and expression pedal calibration
procedures as the original Behringer firmware. Therefore, calibration
instructions can be found in the Behringer manual or online by googling for
“FCB1010 calibration”.

- Self test : keep footswitches 1+3 pressed during startup
- Calibration : keep footswitches 1+5 pressed during startup

The factory presets available in the Behringer firmware are no longer available
:

- V-AMP factory preset : keep footswitches 1+6 pressed during startup
- Behringer guitar amp factory preset : keep footswitches 1+7 pressed during
  startup
- BASS V-AMP factory preset : keep footswitches 1+8 pressed during startup

Instead, there is a setup reset which clears the current UnO2 setup, and a WIFI
reset which resets the IP address, SSID and password of the embedded WIFI access
point to its default values :

- Setup reset : keep footswitches 1+4 pressed during startup
- WIFI reset : keep footswitches 1+2 pressed during startup

Finally, you can toggle the communication between FCB1010 main board and Wino2
module on and off (needs to be on with the Wino2 module installed, but off when
the module is removed).

- Toggle use of Wino2 on/off : keep footswitches 1+9 pressed during startup
