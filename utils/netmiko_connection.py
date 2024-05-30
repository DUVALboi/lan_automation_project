# utils/netmiko_utils.py

from netmiko import ConnectHandler
from utils.logging_config import logger

def configure_device(ip, username, password, commands):
    try:
        device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
        }

        logger.info(f'Connecting to device {ip}...')
        net_connect = ConnectHandler(**device)

        logger.info('Sending configuration commands...')
        output = net_connect.send_config_set(commands)
        logger.info(f'Configuration output: {output}')

        logger.info('Closing connection...')
        net_connect.disconnect()
        logger.info('Connection closed successfully.')
    except Exception as e:
        logger.error(f'Error configuring device {ip}: {e}')
