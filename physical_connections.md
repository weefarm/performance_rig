<!-- @format -->

# Physical Connections - MIDI Guitar Rig

## Connection Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHYSICAL LAYOUT (MIDI RING)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   OFF-BOARD (Floor Chain Loop)                                              │
│   ═══════════════════════════════════════════════════════════════════       │
│                                                                             │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────────────┐      │
│   │  GCP     │───▶│Stock FCB │───▶│  WINO2   │───▶│  HeadRush Prime  │      │
│   │  Ch 4    │    │  Ch 5    │    │ (Looper) │    │  (FX / Producer) │      │
│   └────▲─────┘    └──────────┘    └──────────┘    └────────┬─────────┘      │
│        │                                                   │                │
│ (RING START)                                           (RING END)           │
│        │                                                   │                │
│   ═════│═══════════════════════════════════════════════════│══════════════  │
│   Board Box Passthrough (1x OUT, 1x IN)                    │                │
│   ─────────────────────────────────────────────────────────│──────────────  │
│                                                            │                │
│                                                            │                │
│   ┌──────────────┐          ┌──────────────────┐           │                │
│   │  QuadCortex  │◀──(USB)──▶│ [USB HOST 1]     │           │                │
│   │  (MIDI USB)  │ (BI-DIR) │                  │           │                │
│   └──────────────┘          │                  │           │                │
│                             │                  │           │                │
│                             │       mioXM      │           ▼                │
│   ┌──────────────┐          │                  │   ┌──────────────┐         │
│   │ MIDI PASS OUT│◀─────────┤ [OUT 1]          │   │ MIDI PASS IN │         │
│   │ (Floor Start)│          │                  │   │ (Floor Ret)  │         │
│   └──────────────┘          │       HUB        │   └──────┬───────┘         │
│                             │                  │          │                 │
│                             │ [DIN IN 1]       │◀─────────┘                 │
│                             │                  │                            │
│   ┌──────────────┐          │                  │           │                │
│   │  Microcosm   │◀─────────┤ [OUT 2]          │           │                │
│   │  (MIDI IN)   │          │                  │           │                │
│   └──────────────┘          │                  │           │                │
│                             │                  │           │                │
│   ┌──────────────┐          │                  │           │                │
│   │  Microcosm   │─────────▶│ [DIN IN 2]       │           │                │
│   │  (MIDI OUT)  │          └──────────────────┘           │                │
│   └──────────────┘                                         │                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Cable List

| #   | Cable Type     | From                          | To                       | Length Estimate   |
| --- | -------------- | ----------------------------- | ------------------------ | ----------------- |
| 1   | MIDI 5-pin     | Board PASSTHROUGH [OUT]       | GCP MIDI IN              | 3-5m (Ring Start) |
| 2   | MIDI 5-pin     | GCP MIDI OUT                  | Stock FCB MIDI IN        | 1m (floor chain)  |
| 3   | MIDI 5-pin     | Stock FCB MIDI THRU           | WINO2 MIDI IN            | 1m (floor chain)  |
| 4   | MIDI 5-pin     | WINO2 MIDI OUT                | HRP MIDI IN              | 1m (floor chain)  |
| 5   | MIDI 5-pin     | HRP MIDI OUT                  | Board PASSTHROUGH [IN]   | 3-5m (Ring End)   |
| 6   | MIDI 5-pin     | Board PASSTHROUGH [IN]        | mioXM DIN IN 1           | 0.5m (internal)   |
| 7   | MIDI 5-pin     | mioXM DIN OUT 1               | Board PASSTHROUGH [OUT]  | 0.5m (internal)   |
| 8   | USB A-to-B     | mioXM USB HOST 1              | QuadCortex USB port      | 0.5m (internal)   |
| 9   | TRS 1/4"       | Standalone Pedal 1 (Wah)      | QC Expression 1          | 2-3m              |
| 10  | TRS 1/4"       | Standalone Pedal 2 (Volume)   | QC Expression 2          | 2-3m              |
| 11  | TRS 1/4"       | HRP FX Loop Send (Stereo TRS) | Microcosm Input (TRS)    | 0.5m patch        |
| 12  | Dual TS to TRS | Microcosm Output (L/R TS)     | HRP FX Loop Return (TRS) | 0.5m Y-adapter    |
| 13  | MIDI 5-pin     | mioXM DIN OUT 2               | Microcosm MIDI IN        | 0.5m (internal)   |
| 14  | _(Deleted)_    | —                             | —                        | —                 |
| 15  | MIDI 5-pin     | Microcosm MIDI OUT            | mioXM DIN IN 2           | 0.5m (internal)   |

## mioXM Port Assignments

| Port         | Device        | Software Label | Direction | Channels |
| :----------- | :------------ | :------------- | :-------- | :------- |
| **DIN 1**    | Floor Ring    | `Floor Ring`   | Bi-Dir    | Ch 1-5   |
| **DIN 2**    | Microcosm     | `Microcosm`    | Bi-Dir    | Ch 3     |
| **USB HST1** | QuadCortex    | `QC`           | Bi-Dir    | Ch 1     |
| **DIN 3**    | _(Available)_ | —              | —         | —        |
| **DIN 4**    | _(Available)_ | —              | —         | —        |

## Expression Pedal Connections

| Pedal         | Physical Location         | Cable To        | Target CC           |
| ------------- | ------------------------- | --------------- | ------------------- |
| Standalone 1  | Floor (Direct to QC)      | QC EXP 1 input  | Internal (Wah)      |
| Standalone 2  | Floor (Direct to QC)      | QC EXP 2 input  | Internal (Volume)   |
| GCP EXP 1     | Ground Control Pro jack 1 | Via MIDI to QC  | User assignable     |
| GCP EXP 2     | Ground Control Pro jack 2 | Via MIDI to QC  | User assignable     |
| WINO2 EXP A   | FCB1010 WINO2 internal    | Via MIDI to HRP | CC 11 (Mix)         |
| WINO2 EXP B   | FCB1010 WINO2 internal    | Via MIDI to HRP | CC 12 (FX Loop Mix) |
| HRP Built-in  | On HeadRush Prime         | Internal        | User assignable     |
| Stock EXP A/B | Stock FCB1010             | Via MIDI to HRP | CC 61, 62           |

## Notes

- **Floor Chain**: The Ground Control Pro (GCP), Stock FCB1010, WINO2, and
  HeadRush Prime are all part of a single serial MIDI Ring. Data flows through
  them in order before returning to the mioXM HUB via the "MIDI PASS IN" port.
- Standalone expression pedals connect directly to QC's analog inputs for lowest
  latency and dedicated Wah/Volume control.
- Microcosm receives dedicated MIDI from **mioXM DIN OUT 2** (internal to board
  box).
- The HRP FX Loop is configured as a **Stereo Loop**, using TRS jacks for both
  Send and Return. Due to the Microcosm's layout, this requires a standard TRS
  cable for the Send and a Dual-Mono-TS to Stereo-TRS "Y" cable for the Return.
- **MIDI Ring Topology**: To support HRP as a producer/consumer with 1-IN/1-OUT,
  the gear is wired in a serial loop. Each device must be set to `MIDI THRU: ON`
  or `MIDI MERGE` to ensure signals pass through to the next device.
- **HRP Producer Settings**: Ensure HeadRush Prime is set to `MIDI THRU: ON` to
  pass controller data, and enable `MIDI CLOCK SEND` or similar if you want it
  to produce time data.
- All MIDI cables should be quality 5-pin DIN; avoid cheap cables for
  reliability.
