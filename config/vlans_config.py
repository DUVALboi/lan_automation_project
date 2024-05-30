vlans = {
    # VLAN 10: DNS-1, DNS-2, DNS-4
    # Green: DNS-1, DNS2
    # Yellow: DNS-4

    10: {
        'subnet': '192.168.10.0/24',
        'devices': ['DNS-1', 'DNS-2']
    },

    110: {
        'subnet': '192.169.10.0/24',
        'devices': ['DNS-4']
    },

    # VLAN 20: PC1, DNS-3, PC3
    # Green: PC1, DNS-3
    # Yellow: PC3

    20: {
        'subnet': '192.168.20.0/24',
        'devices': ['PC1', 'DNS-3']
    },

    120: {
        'subnet': '192.169.20.0/24',
        'devices': ['PC3']
    },

    # VLAN 30: PC2, Server_Rack
    30: {
        'subnet': '192.169.30.0/24',
        'devices': ['PC2', 'Server_Rack']
    },

    # VLAN 40: AAA-1
    40: {
        'subnet': '192.168.40.0/24',
        'devices': ['AAA-1']
    },

    # VLAN 98: MGMTyellow
    98: {
        'subnet': '192.169.99.0/24',
        'devices': ['MGMTyellow']
    },

    # VLAN 99: MGMTgreen
    99: {
        'subnet': '192.168.99.0/24',
        'devices': ['MGMTgreen']
    },

    # Special VLAN
    101: 'BlackHole'
}
