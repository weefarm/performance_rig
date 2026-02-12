<!-- @format -->

# MIDI Cable Requirements — All-in-One Board

This table reflects your setup where the **mioXM is mounted underneath the pedal
surface**, requiring only short patch cables for all internal connections.

| #   | Segment          | Source (From)              | Destination (To)           | Type             | Est. Length | Status   |
| :-- | :--------------- | :------------------------- | :------------------------- | :--------------- | :---------- | :------- |
| 1   | **Stage Link**   | Board Box [OUT] (External) | GCP MIDI IN (Floor Start)  | 5-pin DIN        | 10 - 20 ft  | **HAVE** |
| 2   | **Stage Link**   | HRP MIDI OUT (Floor End)   | Board Box [IN] (External)  | 5-pin DIN        | 10 - 20 ft  | **HAVE** |
| 3   | **Internal Box** | mioXM DIN OUT 1            | Board Box [OUT] (Internal) | 5-pin DIN        | 1 - 3 ft    | Need     |
| 4   | **Internal Box** | Board Box [IN] (Internal)  | mioXM DIN IN 1             | 5-pin DIN        | 1 - 3 ft    | Need     |
| 5   | **Internal Box** | mioXM DIN OUT 2            | Microcosm MIDI IN          | 5-pin DIN        | 1 - 3 ft    | Need     |
| 6   | **Internal Box** | Microcosm MIDI OUT         | mioXM DIN IN 2             | 5-pin DIN        | 1 - 3 ft    | Need     |
| 7   | **Floor Chain**  | GCP MIDI OUT               | Stock FCB MIDI IN          | 5-pin DIN        | 1 ft        | Need     |
| 8   | **Floor Chain**  | Stock FCB MIDI THRU        | WINO2 MIDI IN (Internal)   | 5-pin DIN        | 0.5 ft      | Need     |
| 9   | **Floor Chain**  | WINO2 MIDI OUT             | HeadRush Prime MIDI IN     | 5-pin DIN        | 1 ft        | Need     |
| 10  | **Data Link**    | mioXM USB HOST 1           | Quad Cortex USB port       | USB (A-to-B)     | 1 - 3 ft    | Need     |
| 11  | **Data Link**    | mioXM USB HOST 2           | Pico 2 W MIDI Translator   | USB (A-to-Micro) | 0.5 - 1 ft  | Need     |

## Buying List Summary:

To complete the rig, you will need:

- **7x Short MIDI DIN Cables** (1-3 ft or "patch" length).
- **1x USB A-to-B Cable** (Standard printer style for QC).
- **1x USB A-to-Micro Cable** (For the Pico 2 W).

### Note on "Board Box"

The "Board Box" bridges your floor chain to the hidden mioXM. Your long stage
cables (#1 and #2) connect to the outside of the box. Everything else is tucked
away inside.
