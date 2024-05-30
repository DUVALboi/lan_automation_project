from utils.netmiko_connection import configure_device
from config.device_config import devices
from utils.logging_config import logger

commands = {
    'router': ['interface vlan 10', 'ip address 192.168.10.1 255.255.255.0', 'no shutdown'],
    'switch': ['vlan 10', 'name VLAN_10']
}

def configure_devices():
    for device in devices:
        try:
            logger.info(f'Configuring device {device["ip"]} ({device["type"]})...')
            configure_device(device['ip'], device['username'], device['password'], commands[device['type']])
            logger.info(f'Device {device["ip"]} configured successfully.')
        except Exception as e:
            logger.error(f'Failed to configure device {device["ip"]}: {e}')
