#include <Arduino.h>
#include <USB.h>
#include <USBMIDI.h>

/**
 * MIDI Translator for Performance Rig
 * Device: Arduino Nano ESP32 (ESP32-S3)
 * 
 * Logic:
 * - Listens for Program Changes (PC) from floor controllers
 * - Translates PC to Control Change (CC) for destination devices
 * - Handles QC (Ch 1), HRP (Ch 2), and Microcosm (Ch 3)
 */

USBMIDI MIDI;

// --- CONFIGURATION ---
const int GCP_CHANNEL  = 4;  // Incoming Channel for Ground Control Pro
const int STOCK_CHANNEL = 5; // Incoming Channel for Stock FCB1010

const int QC_CHANNEL    = 1;  // Outgoing Channel for Quad Cortex
const int HRP_CHANNEL   = 2;  // Outgoing Channel for HeadRush Prime
const int MC_CHANNEL    = 3;  // Outgoing Channel for Microcosm

// --- CALLBACK FUNCTIONS ---

void handleProgramChange(byte channel, byte number) {
    // 1. Handle Ground Control Pro (GCP) Remapping (Channel 4)
    // Goal: Support "Zero-Config" where GCP sends raw PC 0-127
    if (channel == GCP_CHANNEL) {
        // Map PC 0-7 to QC Stomps A-H (CC 35-42)
        if (number <= 7) { 
            MIDI.controlChange(QC_CHANNEL, 35 + number, 127);
        }
        // Map PC 8-11 to QC Scenes A-H (Bank 0: 8-11, Bank 1: 12-15, etc.)
        else if (number >= 8 && number <= 15) {
            // Note: number 8 (PC 8) -> CC 80 (Scene A)
            MIDI.controlChange(QC_CHANNEL, 72 + number, 127); 
        }
    }
    
    // 2. Handle Stock FCB1010 Remapping (Channel 5)
    else if (channel == STOCK_CHANNEL) {
        // Map PC 0-7 to HRP Block Toggles 1-8 (CC 75-82)
        if (number <= 7) {
            MIDI.controlChange(HRP_CHANNEL, 75 + number, 127);
        }
        // Map PC 8-9 to Rig Up/Down
        else if (number == 8) MIDI.controlChange(HRP_CHANNEL, 17, 127); // Prev
        else if (number == 9) MIDI.controlChange(HRP_CHANNEL, 16, 127); // Next
    }
}

void handleControlChange(byte channel, byte controller, byte value) {
    // 1. Handle GCP Expression Pedals (Channel 4)
    if (channel == GCP_CHANNEL) {
        if (controller == 1)      MIDI.controlChange(QC_CHANNEL, 1, value); // Wah
        else if (controller == 2) MIDI.controlChange(QC_CHANNEL, 2, value); // Volume
    }
    // 2. Handle Stock FCB Expression Pedals (Channel 5)
    else if (channel == STOCK_CHANNEL) {
        if (controller == 7)       MIDI.controlChange(HRP_CHANNEL, 61, value); // Exp A to Param 1
        else if (controller == 27) MIDI.controlChange(HRP_CHANNEL, 62, value); // Exp B to Param 2
    } 
    // Pass through everything else
    else {
        MIDI.controlChange(channel, controller, value);
    }
}

void setup() {
    MIDI.begin();
}

void loop() {
    // Check for incoming USB MIDI messages
    if (MIDI.read()) {
        byte type    = MIDI.getType();
        byte channel = MIDI.getChannel();
        byte data1   = MIDI.getData1();
        byte data2   = MIDI.getData2();

        switch (type) {
            case 0xC0: // Program Change
                handleProgramChange(channel, data1);
                break;
            case 0xB0: // Control Change
                handleControlChange(channel, data1, data2);
                break;
            case 0xF8: // Timing Clock
            case 0xFA: // Start
            case 0xFB: // Continue
            case 0xFC: // Stop
                // Pass through Realtime messages untouched for sync
                MIDI.sendRealTime(type);
                break;
            default:
                // Pass through everything else untouched
                MIDI.sendRaw(type, data1, data2);
                break;
        }
    }
}
