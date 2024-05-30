devices = [
    # Green Zone
    {'name': 'Switch_1_Green', 'ip': '192.168.99.1', 'type': 'switch', 'vlan': 99},
    {'name': 'Switch_2_Green', 'ip': '192.168.99.2', 'type': 'switch', 'vlan': 99},
    {'name': 'Switch_3_Green', 'ip': '192.168.99.3', 'type': 'switch', 'vlan': 99},
    {'name': 'Switch_4_Green', 'ip': '192.168.99.4', 'type': 'switch', 'vlan': 99},
    {'name': 'Switch_5_Green', 'ip': '192.168.99.254', 'type': 'switch', 'vlan': 99, 'gateway': '192.168.99.254'},

    {'name': 'DNS-1', 'ip': '192.168.10.1', 'type': 'pc', 'vlan': 10, 'gateway': '192.168.10.254'},
    {'name': 'DNS-2', 'ip': '192.168.10.2', 'type': 'pc', 'vlan': 10, 'gateway': '192.168.10.254'},
    {'name': 'PC-1', 'ip': '192.168.20.1', 'type': 'pc', 'vlan': 20, 'gateway': '192.168.20.254'},
    {'name': 'DNS-3', 'ip': '192.168.20.2', 'type': 'pc', 'vlan': 20, 'gateway': '192.168.20.254'},

    # Yellow Zone
    {'name': 'Switch_1_Yellow', 'ip': '192.169.98.1', 'type': 'switch', 'vlan': 98},
    {'name': 'Switch_2_Yellow', 'ip': '192.169.98.2', 'type': 'switch', 'vlan': 98},
    {'name': 'Switch_3_Yellow', 'ip': '192.169.98.3', 'type': 'switch', 'vlan': 98},
    {'name': 'Switch_4_Yellow', 'ip': '192.169.98.4', 'type': 'switch', 'vlan': 98, 'gateway': '192.169.98.254'},

    {'name': 'DNS-4', 'ip': '192.169.10.1', 'type': 'pc', 'vlan': 10, 'gateway': '192.169.10.254'},
    {'name': 'PC-3', 'ip': '192.169.20.1', 'type': 'pc', 'vlan': 20, 'gateway': '192.169.20.254'},
    {'name': 'Server_Rack', 'ip': '192.169.30.1', 'type': 'pc', 'vlan': 30, 'gateway': '192.169.30.254'},
    {'name': 'PC-2', 'ip': '192.169.30.2', 'type': 'pc', 'vlan': 30, 'gateway': '192.169.30.254'},

    # Blue Zone
    {'name': 'Switch_Blue', 'ip': '192.168.40.100', 'type': 'switch', 'vlan': 40},
    {'name': 'AAA-1', 'ip': '192.168.40.1', 'type': 'pc', 'vlan': 40},
    {'name': 'vRouter-1', 'ip': '192.168.40.254', 'type': 'router', 'gateway': '192.168.40.254'},

    # Interfaces
    {'name': 'Switch_5_Green', 'ip': '192.168.99.5', 'type': 'switch', 'vlan': 99, 'gateway': '192.168.99.254'},
    {'name': 'vRouter-2', 'ip': '11.11.11.1', 'type': 'router'},
    {'name': 'vRouter-3', 'ip': '12.12.12.1', 'type': 'router'},
    {'name': 'NAT', 'ip': '209.150.53.1', 'type': 'router'},

    # Connections
    {'name': 'vRouter-1_to_Switch_5_Green', 'type': 'connection', 'interface': 'g1/1', 'device': 'Switch_5_Green', 'ip': '200.0.150.1'},
    {'name': 'vRouter-1_to_Switch_5_Green', 'type': 'connection', 'interface': 'g1/3', 'device': 'vRouter-1', 'ip': '200.0.150.2'},
    {'name': 'vRouter-3_to_Switch_4_Yellow', 'type': 'connection', 'interface': 'g0/0', 'device': 'Switch_4_Yellow', 'ip': '200.100.150.1'},
    {'name': 'vRouter-3_to_Switch_4_Yellow', 'type': 'connection', 'interface': 'g0/0', 'device': 'vRouter-3', 'ip': '200.100.150.2'},
    {'name': 'vRouter-1_to_vRouter-2', 'type': 'connection', 'interface': 'g1/2', 'device': 'vRouter-2', 'ip': '11.11.11.2'},
    {'name': 'vRouter-2_to_vRouter-3', 'type': 'connection', 'interface': 'g1/2', 'device': 'vRouter-3', 'ip': '12.12.12.2'},
    {'name': 'vRouter-2_to_NAT', 'type': 'connection', 'interface': 'g1/3', 'device': 'NAT', 'ip': '209.150.53.2'}
]
