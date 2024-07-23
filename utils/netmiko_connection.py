import logging
from netmiko import ConnectHandler

logger = logging.getLogger(__name__)

def create_connection(device):
    try:
        logger.info(f"Attempting to connect to device: {device['ip']} on port {device.get('port', 22)}")
        connection = ConnectHandler(**device)
        logger.info(f"Connection established to device: {device['ip']}")
        return connection
    except Exception as e:
        logger.error(f"Failed to connect to device: {device['ip']}. Error: {e}")
        return None

def send_commands(connection, commands):
    try:
        logger.info(f"Sending commands to device: {connection.host}")
        output = connection.send_config_set(commands)
        logger.info(f"Commands sent successfully to device: {connection.host}")
        return output
    except Exception as e:
        logger.error(f"Failed to send commands to device: {connection.host}. Error: {e}")
        return None

def save_configuration(connection):
    try:
        logger.info(f"Saving configuration on device: {connection.host}")
        connection.save_config()
        logger.info(f"Configuration saved successfully on device: {connection.host}")
    except Exception as e:
        logger.error(f"Failed to save configuration on device: {connection.host}. Error: {e}")

def close_connection(connection):
    try:
        logger.info(f"Closing connection to device: {connection.host}")
        connection.disconnect()
        logger.info(f"Connection closed to device: {connection.host}")
    except Exception as e:
        logger.error(f"Failed to close connection to device: {connection.host}. Error: {e}")
