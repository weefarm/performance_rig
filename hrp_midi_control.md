<!-- @format -->

# HeadRush Prime MIDI Parameter Control

This guide explains how to map the **Stock FCB1010** (Channel 5) to control
specific parameters on the HeadRush Prime (HRP).

## 1. Global Parameter Knobs (Auto-Mapping)

The HRP exposes its three on-screen parameter knobs via MIDI CC. These
automatically control whatever is focused on the screen.

| Target Knob | MIDI CC# | Recommended Stock FCB Control |
| ----------- | -------- | ----------------------------- |
| Top Knob    | CC 61    | Expression Pedal A            |
| Middle Knob | CC 62    | Expression Pedal B            |
| Bottom Knob | CC 63    | (Available for Switch)        |

## 2. Hard-Mapping Specific Parameters

If you want a pedal/switch to **always** control a specific parameter (e.g.,
Delay Feedback) regardless of what is focused:

1.  **Select a Block**: Double-tap any block in your rig (e.g., "Air Delay").
2.  **Enter Hardware Assign**: Tap the **Hardware Assign** icon (3 dots/lines)
    in the top-right corner.
3.  **Choose a Slot**: Tap an empty assignment slot.
4.  **Set Source**: Set the source to **MIDI CC**.
5.  **Set CC#**: Enter the CC number sent by your Stock FCB (e.g., 61).
6.  **Set Parameter**: Select the parameter (e.g., "Mix").
7.  **Set Range**: Adjust the Min/Max values if you want the pedal to only sweep
    a specific range.

## 3. Stock FCB1010 Recommended Layout

| Switch | Function          | HRP CC# |
| ------ | ----------------- | ------- |
| 1-8    | Block Toggle 1-8  | 75-82   |
| 9      | Rig Down (Prev)   | 17      |
| 10     | Rig Up (Next)     | 16      |
| Exp A  | Top Param Knob    | 61      |
| Exp B  | Middle Param Knob | 62      |

> **Note**: These assignments assume your Stock FCB is sending on **Channel 5**.
> The mioXM will automatically remap these to the HRP on Channel 2.
