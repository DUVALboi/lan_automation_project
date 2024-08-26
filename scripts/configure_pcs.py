# configure_pcs.py

from utils.ssh_connection import SSHConnection
from config.device_config import devices

def assign_device_ips():
    print("\nAssigning IP addresses to end devices...")

    # This is a placeholder for actual DHCP or manual IP assignment logic.
    # Depending on your environment, you'd automate DHCP server configuration or manually assign IPs.
    
    # For demonstration, this simply prints out a message.
    for device_name, device_info in devices.items():
        print(f"Assigning IP to devices connected to {device_name}...")
        connection = SSHConnection(device_info)
        
        # Placeholder logic to configure DHCP on the device (example)
        dhcp_commands = [
            "ip dhcp excluded-address 192.168.10.1 192.168.10.10",
            "ip dhcp pool VLAN10",
            "network 192.168.10.0 255.255.255.0",
            "default-router 192.168.10.1",
            "lease 7"
        ]
        
        connection.send_config_commands(dhcp_commands)
    
    print("IP addresses have been assigned.")

