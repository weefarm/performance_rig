<!-- @format -->

# Ground Control Pro Configuration

## Global Settings

| Setting            | Value   | Notes                                         |
| ------------------ | ------- | --------------------------------------------- |
| Presets Per Bank   | 4       | Enables 8 instant access switches             |
| MIDI Channel       | 4       | All commands sent on Ch 4 for mioXM remapping |
| Expression Pedal 1 | Enabled | CC 1 (Wah)                                    |
| Expression Pedal 2 | Enabled | CC 2 (Volume)                                 |

## Footswitch Layout

```
┌────────────────────────────────────────────────────────────────┐
│                    GROUND CONTROL PRO                          │
│                  (4 Presets/Bank Mode)                         │
├────────────┬────────────┬────────────┬────────────┬───────────┤
│    [1]     │    [2]     │    [3]     │    [4]     │           │
│  QC STOMP  │  QC STOMP  │  QC STOMP  │  QC STOMP  │   [UP]    │
│     A      │     B      │     C      │     D      │   BANK    │
│  CC 35     │  CC 36     │  CC 37     │  CC 38     │           │
├────────────┼────────────┼────────────┼────────────┼───────────┤
│    [5]     │    [6]     │    [7]     │    [8]     │           │
│  QC STOMP  │  QC STOMP  │  QC STOMP  │  QC STOMP  │  [DOWN]   │
│     H      │     E      │     F      │     G      │   BANK    │
│  CC 42     │  CC 39     │  CC 40     │  CC 41     │           │
├────────────┴────────────┴────────────┴────────────┴───────────┤
│    [9]     │   [10]     │   [11]     │   [12]     │  [EDIT]   │
│  SCENE A   │  SCENE B   │  SCENE C   │  SCENE D   │           │
│  CC 80     │  CC 81     │  CC 82     │  CC 83     │           │
└────────────┴────────────┴────────────┴────────────┴───────────┘
```

## Instant Access Switch Assignments (1-8)

| Switch | Function   | CC# | Mode            | LED Behavior         |
| ------ | ---------- | --- | --------------- | -------------------- |
| 1      | QC Stomp A | 35  | Normal (toggle) | ON when stomp active |
| 2      | QC Stomp B | 36  | Normal (toggle) | ON when stomp active |
| 3      | QC Stomp C | 37  | Normal (toggle) | ON when stomp active |
| 4      | QC Stomp D | 38  | Normal (toggle) | ON when stomp active |
| 5      | QC Stomp H | 42  | Normal (toggle) | ON when stomp active |
| 6      | QC Stomp E | 39  | Normal (toggle) | ON when stomp active |
| 7      | QC Stomp F | 40  | Normal (toggle) | ON when stomp active |
| 8      | QC Stomp G | 41  | Normal (toggle) | ON when stomp active |

## Preset Assignments (9-12)

Bank 0 sends QC Scenes A-D. Use bank switches for E-H:

| Preset | Bank 0  | Bank 1  | CC Sent |
| ------ | ------- | ------- | ------- |
| 9      | Scene A | Scene E | 80 / 84 |
| 10     | Scene B | Scene F | 81 / 85 |
| 11     | Scene C | Scene G | 82 / 86 |
| 12     | Scene D | Scene H | 83 / 87 |

## Expression Pedal Configuration

| Pedal | CC# | Channel              | Target           |
| ----- | --- | -------------------- | ---------------- |
| EXP 1 | 1   | 4 (via mioXM → Ch 1) | QC Wah           |
| EXP 2 | 2   | 4 (via mioXM → Ch 1) | QC Master Volume |

> **Note**: GCP expression pedals output MIDI CC. The mioXM routes Ch 4 CC 1-2
> to QC on Ch 1. Alternatively, connect EXP pedals directly to QC's analog
> inputs for lowest latency (recommended).

## Setup Steps

### Enable 4 Presets/Bank Mode

1. Press both `[SETUP MODE]` buttons simultaneously
2. Navigate to `PRST/BNK` setting
3. Set to `4 PRSTS`
4. Exit setup (press either `[SETUP MODE]`, then `[+/YES]`)

### Configure Instant Access Switches

1. Enter Setup Mode
2. Navigate to `IA SWTCH`
3. For each switch 1-8:
    - Set CC number as listed above
    - Set Channel to 4
    - Set Mode (Normal or Momentary)
4. Exit and save

### Configure Presets

1. Select preset 9
2. Program: CC 80, value 127, Ch 4
3. Repeat for presets 10-12 with CC 81-83
4. Create Bank 1 with CC 84-87 for Scenes E-H

### Configure Expression Pedals

1. Enter Setup Mode
2. Navigate to `PEDAL`
3. Enable Pedal 1: CC 1, Ch 4
4. Enable Pedal 2: CC 2, Ch 4
