<!-- @format -->

# Physical Connections - MIDI Guitar Rig

## Connection Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHYSICAL LAYOUT                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   OFF-BOARD (Floor)                                                         │
│   ═══════════════════════════════════════════════                           │
│                                                                             │
│   ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐     │
│   │ Ground Ctrl Pro  │    │  Stock FCB1010   │    │  FCB1010 WINO2   │     │
│   │ (scenes/stomps)  │    │  (HRP params)    │    │  (primary ctrl)  │     │
│   │ [MIDI OUT]───────┼───▶│[MIDI IN] [OUT]───┼───▶│[MIDI IN] [OUT]───┼──┐  │
│   └──────────────────┘    └──────────────────┘    └──────────────────┘  │  │
│                                (MERGE)                 (MERGE)          │  │
│                                                                         │  │
│   ┌──────────────────┐                                                  │  │
│   │ HeadRush Prime   │◀───────────────────────────────────────────────┐ │  │
│   │ (Main Looper/FX) │                                                │ │  │
│   │   [MIDI IN]      │                                                │ │  │
│   └──────────────────┘                                                │ │  │
│         ▲                                                             │ │  │
│   ══════│═════════════════════════════════════════════════════════════│═│══ │
│         │                                                             │ │  │
│   PEDALBOARD (Box / Internal)                                         │ │  │
│   ────────────────────────────────────────────────────────────        │ │  │
│         │                                                             │ │  │
│   ┌─────┴────────┐    ┌──────────────────────────────────────────┐    ┌─────────┴─▼──┐ │
│   │ PASSTHROUGH  │    │                mioXM Hub                 │    │ PASSTHROUGH  │ │
│   │    [OUT]     │◀───┤[OUT 2]  [OUT 3]  [OUT 1]  [DIN IN 1]     │◀───┤     [IN]     │ │
│   └──────────────┘    └───────────┬────────┬──────────────▲──────┘    └──────────────┘ │
│                                   │        │              │                            │
│                                   ▼        ▼              │                            │
│                             ┌──────────┐ ┌──────────┐ ┌─────┴────┐                     │
│                             │Microcosm │ │QuadCortex│ │(Floor    │                     │
│                             │  Ch 3    │ │  Ch 1    │ │  Trunk)  │                     │
│                             │ [MIDI IN]│ │ [MIDI IN]│ └──────────┘                     │
│                             └──────────┘ └──────────┘                                  │
│                               │  │                                          │
│                          ┌────┴──┴─────┐                                    │
│                          │ Standalone  │                                    │
│                          │ EXP 1 & 2   │                                    │
│                          └─────────────┘                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Cable List

| #   | Cable Type     | From                          | To                       | Length Estimate  |
| --- | -------------- | ----------------------------- | ------------------------ | ---------------- |
| 1   | MIDI 5-pin     | GCP MIDI OUT                  | Stock FCB MIDI IN        | 1m (floor chain) |
| 2   | MIDI 5-pin     | Stock FCB MIDI OUT            | WINO2 MIDI IN            | 1m (floor chain) |
| 3   | MIDI 5-pin     | WINO2 MIDI OUT                | Board PASSTHROUGH [IN]   | 3-5m (Main Link) |
| 4   | MIDI 5-pin     | Board PASSTHROUGH [IN]        | mioXM DIN IN 1           | 0.5m (internal)  |
| 5   | MIDI 5-pin     | mioXM DIN OUT 2               | Board PASSTHROUGH [OUT]  | 0.5m (internal)  |
| 6   | MIDI 5-pin     | Board PASSTHROUGH [OUT]       | HRP MIDI IN              | 3-5m (Main Link) |
| 7   | MIDI 5-pin     | mioXM DIN OUT 1               | QuadCortex MIDI IN       | 0.5m (internal)  |
| 6   | TRS 1/4"       | Standalone Pedal 1 (Wah)      | QC Expression 1          | 2-3m             |
| 7   | TRS 1/4"       | Standalone Pedal 2 (Volume)   | QC Expression 2          | 2-3m             |
| 8   | TRS 1/4"       | HRP FX Loop Send (Stereo TRS) | Microcosm Input (TRS)    | 0.5m patch       |
| 9   | Dual TS to TRS | Microcosm Output (L/R TS)     | HRP FX Loop Return (TRS) | 0.5m Y-adapter   |
| 10  | MIDI 5-pin     | mioXM DIN OUT 3               | Microcosm MIDI IN        | 0.5m (internal)  |

## mioXM Port Assignments

| Port      | Device                            | Direction | MIDI Channels |
| --------- | --------------------------------- | --------- | ------------- |
| DIN IN 1  | FCB1010 WINO2 (+ Stock via daisy) | Input     | Ch 1, 2, 3, 5 |
| DIN IN 2  | Ground Control Pro                | Input     | Ch 4          |
| DIN IN 3  | _(Available)_                     | —         | —             |
| DIN IN 4  | _(Available)_                     | —         | —             |
| DIN OUT 1 | QuadCortex                        | Output    | Ch 1 only     |
| DIN OUT 2 | HeadRush Prime                    | Output    | Ch 2          |
| DIN OUT 3 | Microcosm                         | Output    | Ch 3          |
| DIN OUT 4 | _(Available)_                     | —         | —             |

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

- The Stock FCB1010 daisy-chains into the WINO2's MIDI IN, then consolidates to
  one cable to mioXM
- Standalone expression pedals connect directly to QC's analog inputs for lowest
  latency and dedicated Wah/Volume control.
- GCP expression pedals connect to the GCP hardware and send MIDI CC data via
  the MIDI chain.
- Microcosm receives MIDI from HRP MIDI THRU chain; mioXM routes Ch 3 to DIN OUT
  2
- The HRP FX Loop is configured as a **Stereo Loop**, using TRS jacks for both
  Send and Return. Due to the Microcosm's layout, this requires a standard TRS
  cable for the Send and a Dual-Mono-TS to Stereo-TRS "Y" cable for the Return.
- All MIDI cables should be quality 5-pin DIN; avoid cheap cables for
  reliability
