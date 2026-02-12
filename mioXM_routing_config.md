<!-- @format -->

# mioXM Configuration Guide (AuracleX)

This document provides the exact settings for the **Auracle for X-Series
(AuracleX)** software.

> [!IMPORTANT] **Logic Reminder**: In AuracleX, a **HIGHLIGHTED** (selected) box
> or button means the signal is **BLOCKED/FILTERED**. A clear (unselected) box
> means the signal is **ENABLED**.

---

## 0. Port Labeling

Before configuring routing, rename your ports in AuracleX to match these labels.

| Physical Port  | Software Label | Connected Device             |
| :------------- | :------------- | :--------------------------- |
| **DIN 1**      | `Floor Ring`   | Floor Ring (GCP → FCB → HRP) |
| **DIN 2**      | `Microcosm`    | Microcosm MIDI IN/OUT        |
| **USB HOST 1** | `QC`           | QuadCortex (Bi-Dir)          |

---

## 1. MIDI Routing

The **Routing** page connects Inputs (left) to Outputs (top).

### Routing Matrix

| Input Port (Source)    | Destination Ports (Enabled) | Purpose                       |
| :--------------------- | :-------------------------- | :---------------------------- |
| **DIN 1** (Floor Ring) | **USB HOST 1**, **DIN 2**   | Main floor chain distribution |
| **USB HOST 1** (QC)    | **DIN 1**, **DIN 2**        | QC control of HRP and Sync    |
| **DIN 2** (Microcosm)  | **USB HOST 1**, **DIN 1**   | Microcosm Sync to rig         |

---

## 2. Filter & Remap

Grouped by physical port pair. Highlights in AuracleX mean **BLOCKED**.

### DIN 1: Floor Ring

#### Input Filters

- **System**: Highlight **Active Sensing** only; others unhighlighted.
- **Channel (1-16)**: Highlight **6-16 (All Message Types)** to block.
- **Rationale**: Allow all floor controllers (Ch 1-5); block everything else.

#### Output Filters

- **System**: Highlight **Active Sensing** only; others unhighlighted.
- **Rationale**: Allow Floor Ring to receive master sync from rig.

### DIN 2: Microcosm

#### Input Filters

- **System**: Highlight **Timing Clock, Start, Stop, Continue, Song Position
  Pointer, Time Code Quarter Frame, Active Sensing**; others unhighlighted.
- **Channel (1-16)**: Highlight **1, 2, 4-16 (All Message Types)** to block.
- **Rationale**: Block Microcosm internal clock/transport; only allow produce
  messages on Ch 3.

#### Output Filters

- **System**: Highlight **Active Sensing** only; others unhighlighted.
- **Rationale**: Allow Microcosm to receive master sync/transport from rig.

### USB HOST 1: QC

#### Input Filters

- **System**: Highlight **Timing Clock, Start, Stop, Continue, Song Position
  Pointer, Time Code Quarter Frame, Active Sensing** only; others unhighlighted.
- **Channel (1-16)**: Highlight **2-16 (All Message Types)** to block.
- **Rationale**: Block QC internal clock/transport; only allow produce messages
  on Ch 1.

#### Output Filters

- **System**: Highlight **Active Sensing** only; others unhighlighted.
- **Rationale**: Allow QC to receive master sync from rig.

---

## 3. USB Host Reservation

Ensures the **QuadCortex** always stays on **HST 1**.

1.  Connect QC to any USB Host port.
2.  Open **USB Host Reservation** tab.
3.  Find `QuadCortex` in the connected list.
4.  Set Reservation to **HST 1**.
5.  Click **Save**.

---

## 4. Presets

- **Preset 1**: `Performance_Rig_Main` (Store to device)

---

## 5. RTP/Network MIDI

- **Status**: **All Blocked** (To ensure strictly wired performance).
- Ensure no routes exist between RTP ports and the performance ports.

---

## 6. Firmware

- Ensure mioXM is on the latest firmware version displayed in the **Firmware**
  tab.
