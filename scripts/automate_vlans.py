from utils.netmiko_connection import configure_device
from config.device_config import devices
from config.vlans_config import vlans
from utils.logging_config import logger

vlan_commands = []
for vlan_id, subnet in vlans.items():
    vlan_commands.append(f'vlan {vlan_id}')
    vlan_commands.append(f'name VLAN_{vlan_id}')
    vlan_commands.append('exit')

def automate_vlans():
    for device in devices:
        try:
            logger.info(f'Automating VLANs on device {device["ip"]}...')
            configure_device(device['ip'], device['username'], device['password'], vlan_commands)
            logger.info(f'VLANs on device {device["ip"]} automated successfully.')
        except Exception as e:
            logger.error(f'Failed to automate VLANs on device {device["ip"]}: {e}')
