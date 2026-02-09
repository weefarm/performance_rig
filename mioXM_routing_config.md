<!-- @format -->

# mioXM Routing Configuration

The iConnectivity mioXM acts as the central hub for the performance rig, routing
MIDI between controllers (WINO2, Stock FCB, GCP) and targets (QC, HRP,
Microcosm).

## Channel Mapping

- **Channel 1**: QuadCortex (Main guitar effects + Ambient Looper)
- **Channel 2**: HeadRush Prime (Vocal effects + Song Structure Looper)
- **Channel 3**: Hologram Microcosm (Ambient textures)
- **Channel 4**: Ground Control Pro (Scene/Stomp controller)
- **Channel 5**: Internal system channel for Stock FCB -> WINO2 communication

## Routing Matrix

### DIN IN 1 (FCB1010 WINO2 / Stock)

| Input Channel | Destination | Output Channel | Purpose           |
| ------------- | ----------- | -------------- | ----------------- |
| Ch 1          | DIN OUT 1   | Ch 1           | QC Control        |
| Ch 2          | DIN OUT 2   | Ch 2           | HRP Control       |
| Ch 3          | DIN OUT 2   | Ch 3           | Microcosm Control |

### DIN IN 2 (Ground Control Pro)

| Input Channel | Destination | Output Channel | Purpose          |
| ------------- | ----------- | -------------- | ---------------- |
| Ch 4          | DIN OUT 1   | Ch 1           | QC Scenes/Stomps |
| Ch 4          | DIN OUT 2   | Ch 3           | Microcosm Bypass |

## Remap Rules (GCP Ch 4 -> Targets)

| Source (GCP) | Target (Device) | Transformation                    |
| ------------ | --------------- | --------------------------------- |
| CC 80-87     | QC (Ch 1)       | Remap to CC 43 (Scene Selection)  |
| CC 35-42     | QC (Ch 1)       | Pass-through to CC 35-42 (Stomps) |
| CC 102       | Micro (Ch 3)    | Pass-through to CC 102 (Bypass)   |

### DIN IN 1 (Stock FCB Channel 5)

These rules apply to a Stock FCB1010 after a **Factory Reset** with the Global
MIDI Channel set to **5**.

| Source (Stock Ch 5) | Transformation Type | Target (HRP Ch 2) | Purpose                |
| :------------------ | :------------------ | :---------------- | :--------------------- |
| PC 00-07            | Remap to CC         | CC 75-82          | HRP Block Toggle 1-8   |
| PC 08               | Remap to CC         | CC 17             | Rig Down (Previous)    |
| PC 09               | Remap to CC         | CC 16             | Rig Up (Next)          |
| CC 07 (Exp A)       | Remap to CC         | CC 61             | HRP Top Parameter Knob |
| CC 27 (Exp B)       | Remap to CC         | CC 62             | HRP Mid Parameter Knob |

## Filter Configuration

- **DIN OUT 1 (QC)**: Allow only Ch 1.
- **DIN OUT 2 (HRP/Micro)**: Allow Ch 2 and Ch 3.
