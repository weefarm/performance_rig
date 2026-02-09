<!-- @format -->

# Stock FCB1010 - Setup Guide (Zero-Programming Method)

This method utilizes the **Factory Default** settings of the FCB1010 and
performs all necessary MIDI transformations inside the **mioXM hub**.

## 1. Prepare the Controller

1.  **Factory Reset**: Keep footswitches **1 and 6** pressed during startup to
    restore factory defaults.
2.  **Set Global MIDI Channel**:
    - Hold down **DOWN** for 2.5 seconds to enter Global Setup.
    - Press **UP** to scroll to the MIDI CH LED.
    - Press **1** (or scroll) to select **MIDI Channel 5**.
    - Hold down **DOWN** to exit and save.
3.  **Physical Connection**: Plug Stock FCB [MIDI OUT] into WINO2 [MIDI IN].

## 2. mioXM Remapping Logic

The mioXM is configured to listen on **Channel 5** and perform the following
transformations to **Channel 2 (HRP)**:

| Factory Msg (Ch 5) | Transformation Rule | HRP Target (Ch 2)      |
| :----------------- | :------------------ | :--------------------- |
| **PC 00-07**       | Map to **CC 75-82** | HRP Block Toggle 1-8   |
| **PC 08**          | Map to **CC 17**    | Rig Down (Previous)    |
| **PC 09**          | Map to **CC 16**    | Rig Up (Next)          |
| **CC 07 (Exp A)**  | Map to **CC 61**    | HRP Top Parameter Knob |
| **CC 27 (Exp B)**  | Map to **CC 62**    | HRP Mid Parameter Knob |

## 3. Usage Note

With this setup, the Stock FCB requires **zero per-preset programming**. Every
preset in every bank will perform these same functions, providing a consistent
"HRP Control Surface."

> [!TIP] If you need to control a specific parameter like "Delay Feedback," use
> the **Hardware Assign** menu on the HRP and map the assignment source to
> **MIDI CC 61** or **62**.
