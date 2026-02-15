<!-- @format -->

# MIDI Translator — Setup & Loading Guide (RPi Pico 2W)

Follow these steps to load the
[pico_translator.py](file:///Users/nathantlong/performance_rig/midi_translator/pico_translator.py)
script onto your **Raspberry Pi Pico 2W** using MicroPython.

## 1. Required Software

- **Thonny IDE**: [Download here](https://thonny.org/). This is the easiest way
  to interact with MicroPython on the Pico.
- **MicroPython Firmware**: Ensure your Pico 2W has the latest MicroPython
  firmware installed.

## 2. Hardware Connection

1. Connect the RPi Pico 2W to your Mac via a **USB cable**.
2. Open Thonny IDE.
3. In the bottom right corner of Thonny, click the interpreter settings and
   select **MicroPython (Raspberry Pi Pico)**.
4. Ensure the **RP2350** (Pico 2) backend is selected if prompted.

## 3. Loading the Code

1. In Thonny, go to **File -> Open...** and select the
   [pico_translator.py](file:///Users/nathantlong/performance_rig/midi_translator/pico_translator.py)
   file from this directory.
2. Select **File -> Save copy...** and choose **Raspberry Pi Pico**.
3. Save the file as `main.py` on the device. **Note:** Saving it as `main.py`
   ensures it runs automatically every time the Pico is powered on.
4. (Optional) If you have a `boot.py`, you can save that to the device as well.

## 4. Physical Rig Integration

1. Unplug the Pico 2W from your computer.
2. Plug it into a **USB Host Port** on the back of your **mioXM**.
3. It will power up automatically when the mioXM is on.
4. Update your **AuracleX Routing**: - **DIN 1 (Floor)** -> **USB Host Port**
   (Pico 2W). - **USB Host Port** (Pico 2W) -> **USB Host 1** (QC), **DIN OUT
   1** (HRP), etc. ss
