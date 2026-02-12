<!-- @format -->

# MIDI Translator — Setup & Loading Guide

Follow these steps to load the
[midi_translator.ino](file:///Users/nathantlong/performance_rig/midi_translator.ino)
onto your **Arduino Nano ESP32**.

## 1. Required Software

- **Arduino IDE**: [Download here](https://www.arduino.cc/en/software) (Version
  2.0+ recommended).
- **ESP32 Board Package**:
    1. Open Arduino IDE -> Settings/Preferences.
    2. Add
       `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
       to "Additional Boards Manager URLs".
    3. Go to **Boards Manager** (left sidebar icon), search for `esp32`, and
       install the package by Espressif.
- **libraries**:
    1. Go to **Library Manager** (left sidebar icon).
    2. Search for and install:
        - `MIDI Library` by François Best.
        - `USB-MIDI` by lathoub (or use the built-in ESP32-S3 USB MIDI
          features).

## 2. Hardware Connection

1. Connect the Arduino Nano ESP32 to your Mac via a **USB-C cable**.
2. Select the board in the IDE: **Tools -> Board -> ESP32 -> Arduino Nano
   ESP32**.
3. Select the port: **Tools -> Port -> (Select the Arduino Nano ESP32 port)**.

## 3. Uploading the Code

1. Open the
   [midi_translator.ino](file:///Users/nathantlong/performance_rig/midi_translator.ino)
   file.
2. Click the **Upload** button (Right Arrow icon) in the top left.
3. Once the status bar says "Done uploading," the Arduino is ready.

## 4. Physical Rig Integration

1. Unplug the Arduino from your computer.
2. Plug it into a **USB Host Port** on the back of your **mioXM**.
3. It will power up automatically when the mioXM is on.
4. Update your **AuracleX Routing**:
    - **DIN 1 (Floor)** -> **USB Host 2** (Arduino).
    - **USB Host 2** (Arduino) -> **USB Host 1** (QC), **DIN OUT 1** (HRP), etc.
