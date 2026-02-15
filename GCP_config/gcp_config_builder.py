
import binascii

def create_gcp_config():
    # 1. Initialize full buffer (16,567 bytes)
    # Total Size: 5 (preamble) + 161 (config) + (200 * 82 presets) + 1 (F7) = 16,567
    buffer = bytearray(16567)
    
    # 2. Set Preamble: F0 00 00 07 10
    buffer[0] = 0xF0
    buffer[1] = 0x00
    buffer[2] = 0x00
    buffer[3] = 0x07
    buffer[4] = 0x10
    
    # 3. GLOBAL CONFIG (Offset 5 - 165)
    # Device 1 Name: "QC RIG  " (8 chars)
    name = "QC RIG  "
    for i, char in enumerate(name):
        buffer[5 + i] = ord(char)
    
    # Device 1 MIDI Channel (Offset 64 in Config Block = 5 + 64 = 69)
    # The GCP appears to store 1-indexed values in memory (1=Ch1, 4=Ch4)
    buffer[69] = 0x04 

    # 4. PRESETS (Offset 166 - 16565)
    # Each preset is 82 bytes
    presets = [
        "QC SCENE A", "QC SCENE B", "QC SCENE C", "QC SCENE D",
        "QC SCENE E", "QC SCENE F", "QC SCENE G", "QC SCENE H"
    ]
    
    for p_idx, p_name in enumerate(presets):
        offset = 166 + (p_idx * 82)
        
        # Set Name (10 chars, ASCII)
        padded_name = p_name.ljust(10)
        for i, char in enumerate(padded_name):
            buffer[offset + i] = ord(char)
            
        # Set Device 1 PC (Offset 10 in preset block)
        # Byte 10: Enabled (0x01)
        # Byte 11: Program # (GCP appears to use 0-indexed internally: 0 = PC 0 on wire)
        buffer[offset + 10] = 0x01
        buffer[offset + 11] = p_idx # PC 0, 1, 2... (Sends PC 0, 1, 2... on wire)
        
        # Ensure other devices (2-8) are OFF (0x00 at their 'enabled' byte)
        for dev in range(1, 8):
            buffer[offset + 10 + (dev * 2)] = 0x00

    # 5. Terminator
    buffer[16566] = 0xF7
    
    # 6. Save to file
    output_path = "/Users/nathantlong/performance_rig/GCP_config.syx"
    with open(output_path, "wb") as f:
        f.write(buffer)
    
    print(f"Generated clean configuration: {output_path}")
    print(f"Total size: {len(buffer)} bytes")

if __name__ == "__main__":
    create_gcp_config()
