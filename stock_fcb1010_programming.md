<!-- @format -->

# Stock FCB1010 - Programming Guide

The Stock FCB1010 does not support the text-based programming language used by
WINO2. It must be programmed manually or via a standard SysEx editor.

## Global Setup

- **MIDI Channel**: Set to **Channel 5**.
- **Remapping**: The mioXM is configured to take Channel 5 and remap it to
  **HeadRush Prime (Channel 2)**.

## Switch Assignments (Bank 0)

Each footswitch should be programmed to send a **Control Change (CC)** message
on **Channel 5**.

| Switch | Function           | CC# | Value (Press) |
| :----- | :----------------- | :-- | :------------ |
| 1      | HRP Block 1 Toggle | 75  | 127           |
| 2      | HRP Block 2 Toggle | 76  | 127           |
| 3      | HRP Block 3 Toggle | 77  | 127           |
| 4      | HRP Block 4 Toggle | 78  | 127           |
| 5      | HRP Block 5 Toggle | 79  | 127           |
| 6      | HRP Block 6 Toggle | 80  | 127           |
| 7      | HRP Block 7 Toggle | 81  | 127           |
| 8      | HRP Block 8 Toggle | 82  | 127           |
| 9      | Rig Down (Prev)    | 17  | 127           |
| 10     | Rig Up (Next)      | 16  | 127           |

## Expression Pedals

| Pedal     | Target       | CC# |
| :-------- | :----------- | :-- |
| **EXP A** | HRP Top Knob | 61  |
| **EXP B** | HRP Mid Knob | 62  |

> [!TIP] To control a specific parameter like "Delay Feedback" instead of the
> focused knob, use the **Hardware Assign** menu on the HeadRush Prime and map
> the assignment source to **MIDI CC 61** or **62**.
