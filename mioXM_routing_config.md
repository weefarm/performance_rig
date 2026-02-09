<!-- @format -->

# mioXM Routing Configuration

This document describes the Auracle X configuration for the iConnectivity mioXM
to route MIDI between controllers and target devices.

## Overview

The mioXM acts as the central hub, receiving MIDI from two input sources and
routing to two output destinations with channel filtering and CC remapping.

## Global Settings

```
Device Preset Slot: 1 (of 4 available)
Preset Name: "Guitar Rig Live"
```

## Routing Matrix

### DIN IN 1 → Outputs (FCB1010 WINO2 + Stock)

| Input Channel | Route To                | Output Channel | Notes                                |
| ------------- | ----------------------- | -------------- | ------------------------------------ |
| Ch 1          | DIN OUT 1               | Ch 1           | QC commands (scenes, stomps, looper) |
| Ch 2          | DIN OUT 2               | Ch 2           | HRP commands (looper, blocks)        |
| Ch 3          | DIN OUT 2               | Ch 3           | Microcosm commands                   |
| Ch 5          | _(Internal processing)_ | —              | Stock FCB bank nav triggers          |

### DIN IN 2 → Outputs (Ground Control Pro)

| Input Channel | Route To  | Output Channel | Notes                         |
| ------------- | --------- | -------------- | ----------------------------- |
| Ch 4          | DIN OUT 1 | Ch 1           | After remap: Scenes, Stomps   |
| Ch 4          | DIN OUT 2 | Ch 3           | After remap: Microcosm bypass |

---

## Filter Configuration

### DIN OUT 1 (To QuadCortex)

- **Allow only**: Channel 1
- **Block**: Channels 2-16
- **Message types**: CC, PC, Note (all allowed)

### DIN OUT 2 (To HeadRush Prime → Microcosm)

- **Allow**: Channel 2 (HRP), Channel 3 (Micro)
- **Block**: Channels 1, 4-16
- **Message types**: CC, PC (allowed)

---

## Remap Rules (GCP Ch 4 → Targets)

These rules transform GCP's outgoing messages to the correct format for target
devices.

### Scene Selection (GCP → QC)

The GCP sends CC 80-87 on Ch 4 for scene selection. The mioXM remaps to QC Scene
CC 43:

| GCP Sends (Ch 4) | mioXM Outputs (Ch 1) | Result     |
| ---------------- | -------------------- | ---------- |
| CC 80, value 127 | CC 43, value 0       | QC Scene A |
| CC 81, value 127 | CC 43, value 1       | QC Scene B |
| CC 82, value 127 | CC 43, value 2       | QC Scene C |
| CC 83, value 127 | CC 43, value 3       | QC Scene D |
| CC 84, value 127 | CC 43, value 4       | QC Scene E |
| CC 85, value 127 | CC 43, value 5       | QC Scene F |
| CC 86, value 127 | CC 43, value 6       | QC Scene G |
| CC 87, value 127 | CC 43, value 7       | QC Scene H |

### Stomp Control (GCP → QC)

GCP sends CC 35-42 on Ch 4. These pass through with channel change only:

| GCP Sends (Ch 4)   | mioXM Outputs (Ch 1) | Result            |
| ------------------ | -------------------- | ----------------- |
| CC 35, value 127/0 | CC 35, value 127/0   | QC Stomp A toggle |
| CC 36, value 127/0 | CC 36, value 127/0   | QC Stomp B toggle |
| CC 37, value 127/0 | CC 37, value 127/0   | QC Stomp C toggle |
| CC 38, value 127/0 | CC 38, value 127/0   | QC Stomp D toggle |
| CC 39, value 127/0 | CC 39, value 127/0   | QC Stomp E toggle |
| CC 40, value 127/0 | CC 40, value 127/0   | QC Stomp F toggle |
| CC 41, value 127/0 | CC 41, value 127/0   | QC Stomp G toggle |
| CC 42, value 127/0 | CC 42, value 127/0   | QC Stomp H toggle |

### Microcosm Bypass (GCP → Micro)

| GCP Sends (Ch 4)  | mioXM Outputs (Ch 3) | Result           |
| ----------------- | -------------------- | ---------------- |
| CC 102, value 127 | CC 102, value 127    | Microcosm Engage |
| CC 102, value 0   | CC 102, value 0      | Microcosm Bypass |

---

## Auracle X Configuration Steps

### Step 1: Connect mioXM

1. Connect mioXM to computer via USB
2. Launch Auracle X application
3. Select mioXM device when detected

### Step 2: Configure Routing

1. Go to **Routing** tab
2. For DIN IN 1:
    - Check box for DIN OUT 1 (Ch 1 filter)
    - Check box for DIN OUT 2 (Ch 2, 3 filter)
3. For DIN IN 2:
    - Check box for DIN OUT 1 (with remap rules)
    - Check box for DIN OUT 2 (with remap rules)

### Step 3: Configure Filters

1. Go to **Filter & Remap** tab
2. Select DIN OUT 1:
    - Under Channel Filter, check only Channel 1
3. Select DIN OUT 2:
    - Under Channel Filter, check Channels 2 and 3

### Step 4: Configure Remaps

1. Still in **Filter & Remap** tab
2. Select DIN IN 2 → DIN OUT 1 path
3. Add remap rules for CC 80-87 → CC 43 with value translation
4. Add channel remap: Ch 4 → Ch 1

### Step 5: Save Preset

1. Go to **Presets** tab
2. Select Preset Slot 1
3. Name: "Guitar Rig Live"
4. Click **Store to Device**

### Step 6: Verify

1. Use MIDI Monitor in Auracle X
2. Press switches on WINO2 → verify correct channel/CC on outputs
3. Press switches on GCP → verify remapped messages

---

## Preset Variations (Optional)

You can store up to 4 presets for different scenarios:

| Slot | Name            | Use Case                        |
| ---- | --------------- | ------------------------------- |
| 1    | Guitar Rig Live | Full rig, all routing active    |
| 2    | QC Only         | Only WINO2 → QC, no HRP/Micro   |
| 3    | Practice Mode   | Reduced routing, debug friendly |
| 4    | _(Available)_   | Future use                      |

## Troubleshooting

| Issue                    | Check                                     |
| ------------------------ | ----------------------------------------- |
| No MIDI reaching QC      | Verify DIN OUT 1 cable, check Ch 1 filter |
| No MIDI reaching HRP     | Verify DIN OUT 2 cable, check Ch 2 filter |
| GCP commands not working | Verify remap rules, check Ch 4 → Ch 1/3   |
| Microcosm not responding | Verify Ch 3 routing, check HRP MIDI THRU  |
