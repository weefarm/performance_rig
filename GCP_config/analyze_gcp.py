
import binascii

def parse_gcp_dump(hex_str):
    # Clean the hex string
    hex_str = hex_str.replace(' ', '').replace('\n', '').replace('\r', '')
    data = binascii.unhexlify(hex_str)
    
    print(f"Total Bytes: {len(data)}")
    
    # Preamble: F0 00 00 07 10
    preamble = data[:5]
    print(f"Preamble: {binascii.hexlify(preamble).upper()}")
    
    # Config Block (161 bytes starting at offset 5)
    config = data[5:166]
    
    # Device Names (8 devices, 8 chars each)
    print("\n--- DEVICES ---")
    for i in range(8):
        name = config[i*8:(i+1)*8].decode('ascii', errors='replace')
        channel = config[64+i]
        print(f"Device {i+1}: '{name.strip()}' on Channel {channel + 1}")
        
    # PC Receive Channel
    receive_ch = config[72]
    print(f"GCP Receive Channel: {receive_ch + 1}")

    # Presets (starting at offset 166)
    preset_size = 82
    print("\n--- PRESETS (First 5) ---")
    for p in range(5):
        offset = 166 + (p * preset_size)
        if offset + preset_size > len(data):
            break
        
        p_data = data[offset:offset+preset_size]
        name = p_data[0:10].decode('ascii', errors='replace')
        
        # Device PC values (offset 10 in preset block)
        pcs = []
        for i in range(8):
            enabled = p_data[10 + i*2]
            pc_num = p_data[11 + i*2]
            status = f"PC {pc_num}" if enabled == 1 else "OFF"
            pcs.append(status)
            
        print(f"Preset {p}: '{name.strip()}' -> Devices: {pcs}")


if __name__ == "__main__":
    import sys
    path = "/Users/nathantlong/performance_rig/rig_config.syx"
    with open(path, "rb") as f:
        data = f.read()
    
    # Simple logic to print results
    print(f"Total Bytes: {len(data)}")
    
    # Preamble
    print(f"Preamble: {binascii.hexlify(data[:5]).upper()}")
    
    # Device Config
    print("\n--- DEVICES ---")
    for i in range(8):
        name = data[5 + i*8 : 5 + (i+1)*8].decode('ascii', errors='replace')
        channel = data[5 + 64 + i]
        print(f"Device {i+1}: '{name.strip()}' on Channel {channel + 1}")
        
    print(f"Receive Channel: {data[5 + 72] + 1}")

    # Presets
    print("\n--- PRESETS (First 8) ---")
    for p in range(8):
        offset = 166 + (p * 82)
        name = data[offset : offset+10].decode('ascii', errors='replace')
        
        pcs = []
        for i in range(8):
            enabled = data[offset + 10 + i*2]
            pc_num = data[offset + 11 + i*2]
            pcs.append(f"PC {pc_num}" if enabled == 1 else "OFF")
            
        print(f"Preset {p}: '{name.strip()}' -> Devices: {pcs}")
