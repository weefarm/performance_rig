<!-- @format -->

# Physical Connections - MIDI Guitar Rig

## Connection Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHYSICAL LAYOUT                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   FLOOR (Foot Controllers)                                                  │
│   ═══════════════════════════════════════════════                           │
│                                                                             │
│   ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐     │
│   │  Stock FCB1010   │    │  FCB1010 WINO2   │    │ Ground Ctrl Pro  │     │
│   │  (HRP params)    │    │  (primary ctrl)  │    │  (scenes/stomps) │     │
│   │                  │    │                  │    │                  │     │
│   │ [MIDI OUT]───────┼──▶│[MIDI IN] [MIDI OUT]────┐    [MIDI OUT]   │     │
│   └──────────────────┘    └──────────────────┘    │    └─────┬──────┘     │
│         ▲ EXP A,B              ▲ EXP A,B          │          │            │
│         │                      │                  │          │            │
│         │   (HRP knobs)    │  (HRP mix,       │          │            │
│         │                  │   FX loop mix)   │          │            │
│                                                   │          │            │
│   ═══════════════════════════════════════════════│══════════│════════════ │
│                                                   │          │            │
│   RACK / TABLE                                    ▼          ▼            │
│   ────────────────────────────────────────────────────────────            │
│                                                                           │
│   ┌─────────────────────────────────────────────────────────┐             │
│   │                    mioXM Hub                            │             │
│   │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │             │
│   │  │ DIN IN 1│  │ DIN IN 2│  │DIN OUT 1│  │DIN OUT 2│    │             │
│   │  │ (WINO2) │  │  (GCP)  │  │  (QC)   │  │  (HRP)  │    │             │
│   │  └────▲────┘  └────▲────┘  └────┬────┘  └────┬────┘    │             │
│   └───────┼────────────┼────────────┼────────────┼─────────┘             │
│           │            │            │            │                        │
│   ════════│════════════│════════════│════════════│═══════════════════════ │
│           │            │            │            │                        │
│   STAGE / AMP AREA     │            │            │                        │
│   ─────────────────────│────────────│────────────│────────────────────    │
│                        │            ▼            ▼                        │
│                        │      ┌──────────┐ ┌──────────┐                   │
│                        │      │QuadCortex│ │HeadRush  │                   │
│                        │      │  Ch 1    │ │  Prime   │                   │
│                        │      │          │ │  Ch 2    │                   │
│                        │      │ [MIDI IN]│ │[MIDI IN] │                   │
│                        │      │          │ │          │                   │
│                        │      │ [EXP 1,2]│ │[FX LOOP] │                   │
│                        │      └────▲──▲──┘ └────┬─┬───┘                   │
│                        │           │  │         │ │                       │
│                        │     ┌─────┴──┴──┐ ┌────┴─┴───┐                   │
│                        │     │ Standalone│ │Microcosm │                   │
│                        │     │ EXP 1 & 2 │ │  Ch 3    │                   │
│                        │     │ (Wah/Vol) │ │(Stereo FX│                   │
│                        └─────┴───────────┘ │  Loop)   │                   │
│                                           └──────────┘                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Cable List

| #   | Cable Type    | From                        | To                       | Length Estimate  |
| --- | ------------- | --------------------------- | ------------------------ | ---------------- |
| 1   | MIDI 5-pin    | Stock FCB1010 MIDI OUT      | FCB1010 WINO2 MIDI IN    | 1m (daisy chain) |
| 2   | MIDI 5-pin    | FCB1010 WINO2 MIDI OUT      | mioXM DIN IN 1           | 3-5m             |
| 3   | MIDI 5-pin    | Ground Control Pro MIDI OUT | mioXM DIN IN 2           | 3-5m             |
| 4   | MIDI 5-pin    | mioXM DIN OUT 1             | QuadCortex MIDI IN       | 2-3m             |
| 5   | MIDI 5-pin    | mioXM DIN OUT 2             | HeadRush Prime MIDI IN   | 2-3m             |
| 6   | TRS 1/4"      | Standalone Pedal 1 (Wah)    | QC Expression 1          | 2-3m             |
| 7   | TRS 1/4"      | Standalone Pedal 2 (Volume) | QC Expression 2          | 2-3m             |
| 8   | TRS 1/4" (x2) | HRP FX Loop Send (L/R)      | Microcosm Input (L/R)    | 0.5m patch       |
| 9   | TRS 1/4" (x2) | Microcosm Output (L/R)      | HRP FX Loop Return (L/R) | 0.5m patch       |

## mioXM Port Assignments

| Port      | Device                            | Direction | MIDI Channels |
| --------- | --------------------------------- | --------- | ------------- |
| DIN IN 1  | FCB1010 WINO2 (+ Stock via daisy) | Input     | Ch 1, 2, 3, 5 |
| DIN IN 2  | Ground Control Pro                | Input     | Ch 4          |
| DIN IN 3  | _(Available)_                     | —         | —             |
| DIN IN 4  | _(Available)_                     | —         | —             |
| DIN OUT 1 | QuadCortex                        | Output    | Ch 1 only     |
| DIN OUT 2 | HeadRush Prime                    | Output    | Ch 2, Ch 3    |
| DIN OUT 3 | _(Available)_                     | —         | —             |
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
- The HRP FX Loop is configured as a **Stereo Loop**, using separate TRS jacks
  for Send L/R and Return L/R (4 cables total).
- All MIDI cables should be quality 5-pin DIN; avoid cheap cables for
  reliability
