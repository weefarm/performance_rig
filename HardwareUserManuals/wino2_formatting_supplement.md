<!-- @format -->

# Wino2 Editor — Formatting & Syntax Supplement

This document supplements the official UnO2 ControlCenter manual with practical
formatting rules discovered through hands-on compilation testing with the Wino2
embedded editor. These rules are not always explicit in the manual but are
enforced by the parser.

---

## 1. File Structure Order

The Wino2 editor requires a strict top-to-bottom ordering of definition
sections. **No comments or blank lines may precede the first section.**

```
PRESETS = { ... }      // 1. Name lists (must come first)
EFFECTS = { ... }
TRIGGERS = { ... }
SWEEPS = { ... }

BANKS = { ... }        // 2. Bank definitions

CHANNEL name = N       // 3. Channel assignments
REMOTE_CONTROL_CHANNEL = N

VAR $name = value      // 4. Variable declarations

INIT_FCB = { ... }     // 5. Implementation blocks
TRIGGER_CLICK ...      //    (triggers, effects, sweeps, presets)
EFFECT_ON ...
SWEEP ...
PRESET ...
```

---

## 2. Brace Placement Rules

### Name List Blocks

`PRESETS`, `EFFECTS`, `TRIGGERS`, `SWEEPS`: the opening `{` goes on a **separate
line** after `=`.

```
PRESETS =
{
GOTO_MENU
GOTO_LOOPER
}
```

### Implementation Blocks (Multi-Command)

For `TRIGGER_CLICK`, `TRIGGER_RELEASE`, `EFFECT_ON`, `EFFECT_OFF`, `INIT_FCB`,
and `PRESET` definitions with multiple commands: the opening `{` goes on a
**separate line** after `=`.

```
TRIGGER_CLICK MY_TRIGGER =
{
SendMidi QC CtrlChange 53 127
SendMidi HRP CtrlChange 70 127
}
```

### Single-Command Blocks

Single-command definitions go entirely on **one line**:

```
TRIGGER_CLICK QC_REC_ON = SendMidi QC CtrlChange 53 127
EFFECT_OFF QC_RECORDING = SendTrigger QC_REC_OFF
PRESET PANIC_STOP = SendTrigger GLOBAL_STOP
```

### Conditional Blocks (`if` / `else`)

The opening `{` goes on the **same line** as the `if` or `else` keyword:

```
if ($S10_ACTIVE) {
$S10_HELD = true
if (#CURRENT_BANK == MENU) {
SendTrigger GLOBAL_STOP
}
else {
GotoBank MENU
}
}
```

> [!IMPORTANT] **Key distinction**: `= {` on the same line is **rejected** by
> the parser. `if (condition) {` on the same line is **required** by the parser.

---

## 3. Variable Usage

### Declaration

Variables are declared **once** in the `VAR` section with an initial value:

```
VAR $CC_QC_REC = 53          // numeric (0-127)
VAR $S10_ACTIVE = false      // boolean (true/false)
VAR $songName = "My Song"    // string
```

### Assignment Inside Blocks

Variables can be re-assigned inside any implementation block using the `$name =`
syntax. The `VAR` keyword is **only** used in the declaration section.

```
TRIGGER_CLICK S10_TRIGGER =
{
$S10_ACTIVE = true     // valid: sets boolean
$S10_HELD = false      // valid: sets boolean
}
```

Numeric operations are also supported:

```
$intvar++              // increment
$intvar--              // decrement
$intvar += 10          // add constant
$boolvar = !$boolvar   // invert boolean
```

---

## 4. Conditional Syntax Reference

### Boolean conditions

```
if ($boolvar) { ... }
if (!$boolvar) { ... }
```

### Numeric comparisons

```
if ($intvar > 64) { ... }
if ($intvar == $intvar2) { ... }
```

### Bank comparison

```
if (#CURRENT_BANK == MENU) { ... }
if (#CURRENT_BANK != LOOPER) { ... }
```

### Effect state checks

```
if (EFFECT_ON MICRO_ACTIVE) { ... }
if (EFFECT_OFF QC_PLAYING) { ... }
```

---

## 5. Common Pitfalls

### Self-Referencing Effect Loops

Never use `SwitchOff` on the effect being defined in its own `EFFECT_OFF`
handler. This creates an infinite loop:

```
// BAD — infinite loop!
EFFECT_OFF MICRO_STOP = SwitchOff MICRO_STOP

// GOOD — send a benign MIDI message instead
EFFECT_OFF MICRO_STOP = SendMidi MICRO CtrlChange 31 0
```

### Undefined Bank References

Every bank name used in `GotoBank` must be defined in the `BANKS` section. If a
bank isn't defined yet, either remove the `GotoBank` command or add a
placeholder bank definition.

### Empty Blocks

Avoid empty blocks `{}` — the parser may reject them with "specify at least 1
command." Always include at least one valid command.

### Identifier Declaration

Every preset, effect, trigger, and sweep name used in `BANKS` or logic must be
declared in its respective name list (`PRESETS`, `EFFECTS`, `TRIGGERS`,
`SWEEPS`).

---

## 6. Compilation Process

1. Copy the entire setup text
2. Paste into the Wino2 embedded editor (browser at `192.168.4.1`)
3. The editor compiles in real time as content is pasted
4. Errors appear in ascending line order — fix the first error to reveal the
   next
5. Click **Save** to store the source on the Wino2 module
6. Click **Send** to compile and flash the binary to the FCB1010

> [!TIP] The editor reports statistics on success: preset count, effect count,
> trigger count, sweep count, bank count, and memory usage percentage. Target <
> 100% memory usage (2048 byte limit for setup data).
