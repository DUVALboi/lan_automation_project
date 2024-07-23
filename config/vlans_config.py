vlans = {
    "green": [
        {"id": 10, "name": "VLAN10", "devices": ["192.168.10.254", "192.168.10.253"]},  # DNS-1, DNS-2
        {"id": 20, "name": "VLAN20", "devices": ["192.168.20.22", "192.168.20.254"]},  # webterm1, DNS3
        {"id": 99, "name": "MgmtGreen", "devices": ["192.168.99.2", "192.168.99.3", "192.168.99.4", "192.168.99.5"]}  # Switches
    ],
    "yellow": [
        {"id": 10, "name": "VLAN10", "devices": ["192.169.10.2"]},  # Firefox-1
        {"id": 20, "name": "VLAN20", "devices": ["192.169.20.2"]},  # PC-3
        {"id": 30, "name": "VLAN30", "devices": ["192.169.30.2"]},  # PC-2 (Server_Rack not modified)
        {"id": 98, "name": "MgmtYellow", "devices": ["192.169.98.1", "192.169.98.2", "192.169.98.3"]}  # Switches
    ]
}
