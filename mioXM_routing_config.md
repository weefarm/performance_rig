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

### DIN IN 1 (Controller Trunk / Ring Return)

| Input Channel | Destination | Output Channel | Purpose           |
| ------------- | ----------- | -------------- | ----------------- |
| Ch 1          | DIN OUT 1   | Ch 1           | QC Control        |
| Ch 2          | DIN OUT 2   | Ch 2           | HRP Control       |
| Ch 3          | DIN OUT 3   | Ch 3           | Microcosm Control |
| Ch 4          | DIN OUT 1   | Ch 1           | QC Scenes/Stomps  |
| Ch 4          | DIN OUT 3   | Ch 3           | Microcosm Bypass  |

### DIN IN 2 (QuadCortex Producer)

| Input Channel | Destination | Output Channel | Purpose           |
| ------------- | ----------- | -------------- | ----------------- |
| (Real-Time)   | DIN OUT 2/3 | (Real-Time)    | Looper/Clock Sync |
| Ch 1          | DIN OUT 2   | Ch 2           | QC -> HRP Control |

### DIN IN 3 (Microcosm Producer)

| Input Channel | Destination | Output Channel | Purpose           |
| ------------- | ----------- | -------------- | ----------------- |
| (Real-Time)   | DIN OUT 1/2 | (Real-Time)    | Looper/Clock Sync |

### DIN IN 1 REMAP RULES (Zero-Config Trunk)

#### GCP "Zero-Config" Remapping

These rules apply to the GCP (Channel 1) merged into the main trunk.

| Source (GCP Ch 1) | Transformation Type   | Target (Device) | Purpose                    |
| :---------------- | :-------------------- | :-------------- | :------------------------- |
| **PC 00-03**      | Remap to **CC 43**    | QC (Ch 1)       | Scenes A-D                 |
| **CC 80-87**      | Remap to **CC 35-42** | QC (Ch 1)       | Stomps A-H                 |
| **CC 87 (IA #8)** | Remap to **CC 88**    | WINO2 (Ch 4)    | Master Panic / Global Stop |

#### Stock FCB1010 Remapping

These rules apply to the Stock FCB (Channel 5) merged into the main trunk.

These rules apply to a Stock FCB1010 after a **Factory Reset** with the Global
MIDI Channel set to **5**.

| Source (Stock Ch 5) | Transformation Type | Target (HRP Ch 2) | Purpose                |
| :------------------ | :------------------ | :---------------- | :--------------------- |
| PC 00-07            | Remap to CC         | CC 75-82          | HRP Block Toggle 1-8   |
| PC 08               | Remap to CC         | CC 17             | Rig Down (Previous)    |
| PC 09               | Remap to CC         | CC 16             | Rig Up (Next)          |
| CC 07 (Exp A)       | Remap to CC         | CC 61             | HRP Top Parameter Knob |
| CC 27 (Exp B)       | Remap to CC         | CC 62             | HRP Mid Parameter Knob |

## MIDI Clock & Synchronization

To prevent clock jitter or multiple-master conflicts, the rig follows a **Single
Master** topology.

### The Strategy: HeadRush Prime as Master

The HeadRush Prime (HRP) is designated as the Clock Master because its
**Threshold Start** feature requires it to dictate the shared looper state to
the rest of the rig.

| Device             | Role         | Implementation                                  | Settings                                   |
| :----------------- | :----------- | :---------------------------------------------- | :----------------------------------------- |
| **HeadRush Prime** | **Master**   | Sends Clock/Start/Stop to mioXM via Floor Ring. | `MIDI Clock Send: ON`, `MIDI Thru: ON`     |
| **Quad Cortex**    | **Follower** | Receives Clock from mioXM [OUT 1].              | `MIDI Clock Receive: ON`, `Clock Out: OFF` |
| **Microcosm**      | **Follower** | Receives Clock from mioXM [OUT 3].              | `MIDI Sync: External`                      |
| **mioXM Hub**      | **Arbiter**  | Filters out other clocks; broadcasts HRP Clock. | Routing: `DIN IN 1 -> OUT 1, OUT 3`        |

### Global Tap Tempo (WINO2 FS 10)

- **Flow**: WINO2 (FS 10) sends **CC 93** (Tap) to the entire rig on broadcast.
- **Sync**: Both HRP and QC receive the physical tap. The HRP (Master) then
  stabilizes the MIDI Clock to that tempo and broadcasts the 24ppqn real-time
  clock to the rest of the rig.

> [!IMPORTANT] To avoid feedback loops, the `mioXM` must be configured to
> **Filter MIDI Clock** on `DIN IN 2` (QC) and `DIN IN 3` (MC) if those devices
> are accidentally set to send clock.

## Filter Configuration

- **DIN OUT 1 (QC)**: Allow Ch 1 + MIDI Real-Time.
- **DIN OUT 2 (HRP)**: Allow Ch 2 + MIDI Real-Time.
- **DIN OUT 3 (Micro)**: Allow Ch 3 + MIDI Real-Time.
