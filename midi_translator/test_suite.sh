#!/bin/bash

# MIDI Translator Automation Test Suite
# This script sends all mapped triggers to the Pico 2 W via the mioXM Host Port.
# Reference: /Users/nathantlong/performance_rig/midi_translator/pico_translator.py

DEVICE="mioXM HST 2"
SLEEP=0.5 # Delay between commands to make MIDI Monitor readable

echo "Starting MIDI Translator Test Suite..."
echo "Target Device: $DEVICE"
echo "---------------------------------------"

# 1. GCP (Ch 4) -> QC (Ch 1)
echo "[GCP -> QC] Testing Stomps (PC 0, 4, 7)..."
sendmidi dev "$DEVICE" ch 4 pc 0 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 4 pc 4 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 4 pc 7 && sleep $SLEEP

echo "[GCP -> QC] Testing Scenes (PC 8, 15)..."
sendmidi dev "$DEVICE" ch 4 pc 8 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 4 pc 15 && sleep $SLEEP

echo "[GCP -> QC] Testing Expression (Wah CC 1, Vol CC 2)..."
sendmidi dev "$DEVICE" ch 4 cc 1 64 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 4 cc 2 64 && sleep $SLEEP

echo "---------------------------------------"

# 2. FCB (Ch 5) -> HRP (Ch 2)
echo "[FCB -> HRP] Testing Toggles (PC 0, 7)..."
sendmidi dev "$DEVICE" ch 5 pc 0 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 5 pc 7 && sleep $SLEEP

echo "[FCB -> HRP] Testing Navigation (Prev PC 8, Next PC 9)..."
sendmidi dev "$DEVICE" ch 5 pc 8 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 5 pc 9 && sleep $SLEEP

echo "[FCB -> HRP] Testing Expression (Exp A CC 7, Exp B CC 27)..."
sendmidi dev "$DEVICE" ch 5 cc 7 64 && sleep $SLEEP
sendmidi dev "$DEVICE" ch 5 cc 27 64 && sleep $SLEEP

echo "---------------------------------------"

# 3. Security Checks
echo "[Safety] Testing Passthrough (Ch 10 PC 0)..."
sendmidi dev "$DEVICE" ch 10 pc 0 && sleep 1.0

echo "---------------------------------------"
echo "Test Suite Complete."
echo "Please provide the MIDI Monitor logs for final evaluation."
