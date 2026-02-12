<!-- @format -->

# Performance Rig - Comprehensive Setup Guide

This guide covers the complete configuration of the MIDI Performance Rig,
including physical connections, device settings, hub routing, and operational
workflows.

---

## 1. Physical Setup & Infrastructure

### MIDI Ring Topology

The rig uses a **Serial MIDI Ring** for the floor devices and a
**Hub-and-Spoke** topology via the mioXM for the core processing units.

**Floor Sequence:** `mioXM [OUT 2]` -> `GCP` -> `Stock FCB` -> `WINO2` -> `HRP`
-> `mioXM [IN 1]`.

**Core Processing:** `mioXM` connects to `QC` via **USB** and `Microcosm` via
**DIN**.

> [!IMPORTANT] All devices in the Floor Sequence must have **MIDI THRU** or
> **MIDI MERGE** enabled to ensure messages reach the mioXM hub.

### Cable Connections

| From                        | To                         | Purpose               |
| :-------------------------- | :------------------------- | :-------------------- |
| Board Box (PASSTHROUGH OUT) | Ground Control Pro (IN)    | Ring Start            |
| Ground Control Pro (OUT)    | Stock FCB1010 (IN)         | Floor Chain Loop      |
| Stock FCB1010 (THRU)        | WINO2 FCB1010 (IN)         | Floor Chain Loop      |
| WINO2 FCB1010 (OUT)         | HeadRush Prime (IN)        | Floor Chain Loop      |
| HeadRush Prime (OUT)        | Board Box (PASSTHROUGH IN) | Ring Return           |
| mioXM [USB HOST 1]          | QuadCortex (USB)           | Core Control (BI-DIR) |
| mioXM [OUT 3]               | Microcosm (IN)             | Core Control          |
| Microcosm (OUT)             | mioXM [IN 3]               | MC Producer (Sync/PC) |

---

## 2. Per-Device Configuration

### MIDI Channel Assignments

| Device                   | MIDI Channel                |
| :----------------------- | :-------------------------- |
| QuadCortex (QC)          | 1                           |
| HeadRush Prime (HRP)     | 2                           |
| Microcosm (MC)           | 3                           |
| Ground Control Pro (GCP) | 4                           |
| Stock FCB1010            | 5 (Remapped to 2 via mioXM) |

### Factory Reset & Global Settings

#### Ground Control Pro (GCP)

1.  **Factory Reset**: Press both **[SETUP MODE]** buttons -> Press
    **[UTILITY]** -> Press **[SELECT 2]** twice ("INIT MEM Y/N") -> Press
    **[+/YES]** twice.
2.  **Per-Bank Mode**: Enter Setup -> `UTILITY` -> Press **[SELECT 2]** -> Set
    to `4 PRST/BANK`.
3.  **MIDI Channel**: Set to **Channel 4**.
4.  **Instant Access Programming (Stomps A-H)**:
    - Enter Setup -> Press **[INSTANT ACCESS]**.
    - For Button 1: Set to `CH01 CTL035` (QC Stomp A).
    - For Button 2: Set to `CH01 CTL036` (QC Stomp B).
    - ...repeat through Button 8: Set to `CH01 CTL042` (QC Stomp H).
    - _Note: If IA 8 is needed for WINO2 Global Stop, set it to `CH04 CTL088`._

#### Stock FCB1010

1.  **Factory Reset**: Hold footswitches **1 and 6** during power-up.
2.  **Global Channel**: Hold **DOWN** (2.5s) -> Press **UP** to `MIDI CH` ->
    Select **5** -> Hold **DOWN** to save.
3.  **Programming Presets (HRP Blocks)**:
    - Select a Preset (1-10).
    - Hold **DOWN** (2.5s) to enter Edit mode.
    - Press **UP** (Confirm) -> Press footswitch **1 (PC 1)** to disable PCs.
    - Press footswitch **6 (CC 1)** to enable CC 1.
    - Set CC number to **75** (Block 1 Toggle).
    - Repeat for footswitches 2-8 (CCs 76-82).
    - Hold **DOWN** (2.5s) to save.

#### HeadRush Prime (HRP)

1.  **Clock Master**: Set `MIDI Clock Send: ON`.
2.  **MIDI Thru**: Set `MIDI Thru: ON`.

#### QuadCortex (QC)

1.  **Clock Follower**: Set `MIDI Clock Receive: ON`, `Clock Out: OFF`.

---

## 3. mioXM Setup (AURACLE)

The mioXM acts as the central router and "translator" for the rig.

### Routing Table

| Input Port          | Destination | Rule              | Purpose                        |
| :------------------ | :---------- | :---------------- | :----------------------------- |
| **DIN IN 1** (Ring) | USB HOST 1  | Ch 1 & 4          | Route GCP & WINO2 to QC        |
|                     | DIN OUT 2   | Ch 2 (Remap 5->2) | Route WINO2 & Stock FCB to HRP |
|                     | DIN OUT 3   | Ch 3 & 4          | Route GCP to Microcosm         |

### Filtering & Sync

- **Filter MIDI Clock** on `USB HOST 1` (QC) and `DIN IN 3` (MC) **INPUTS ONLY**
  to prevent loop/jitter.
- **System Filtering**: Ensure `DIN OUT 2` (HRP) has Clock enabled to act as
  Master.

---

## 4. Footswitch Labeling

Use the following terminology for labeling switches on each device:

### Label Terms

- **TEMPO**: Tap Tempo
- **REC**: Record
- **PLAY**: Play
- **DUB**: Overdub
- **HALFSPD**: Half Speed
- **REV**: Reverse

### Device Labeling Tables

| Device                     | Switch          | Label         | Function                       |
| :------------------------- | :-------------- | :------------ | :----------------------------- |
| **QC** (WINO2 Top Row)     | 6               | REC           | QC Looper Record               |
|                            | 7               | PLAY          | QC Looper Play                 |
|                            | 8               | REV           | QC Looper Reverse              |
|                            | 9               | HALFSPD       | QC Looper Half Speed           |
| **HRP** (WINO2 Bottom Row) | 1               | REC           | HRP Looper Record              |
|                            | 2               | PLAY          | HRP Looper Play                |
|                            | 3               | REV           | HRP Looper Reverse             |
|                            | 4               | HALFSPD       | HRP Looper Half Speed          |
| **MC**                     | Button          | REC/DUB       | Microcosm Record/Overdub       |
|                            | Button          | PLAY/STOP     | Microcosm Play/Stop            |
| **Global**                 | WINO2 Switch 10 | TAP/MENU/STOP | Tap Tempo / Menu / Global Stop |

---

## 5. Rig Behavior & Workflow

### Workflow Examples

#### 1. Constructing an Ambient Backdrop

1.  **Engage Microcosm**: Tap the **MC** switch (or GCP IA #5).
2.  **Construct Loop**: Hold the **MC switch** (Smart Switch logic) to engage
    and play phrases into the Microcosm.
3.  **Capture in QC**: While still holding the MC switch, press **QC REC**.
4.  **Finalize**: Release the MC switch and press **QC PLAY**. The Microcosm
    texture is now looping on the QuadCortex.

#### 2. Building a Song Loop

1.  **Start Song**: Press **HRP REC** to begin recording the foundation.
2.  **Play Loop**: Press **HRP PLAY** (or REC again) to begin the loop.
3.  **Layering**: Press **HRP DUB** to add overdub layers.
4.  **Transition**: Use the **RIG VOL** expression pedal to fade the entire wash
    out or back in.

#### 3. Global Control (Switch 10 Logic)

- **Tap Tempo**: Quickly tap **Switch 10** repeatedly for **TEMPO**.
- **Enter Menu**: Hold **Switch 10** for **> 2 seconds**. This takes the WINO2
  to the MENU bank for navigation.
- **Emergency Stop**: While in the **MENU**, hold **Switch 10** for another **2
  seconds** to trigger a **Global Stop** (stops all loopers immediately).

---
