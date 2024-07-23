import logging
from utils.ssh_connection import create_ssh_connection, send_ssh_command, close_ssh_connection
from config.device_config import devices

logger = logging.getLogger(__name__)

def configure_devices(zone):
    """Automate device configuration for a specified zone."""
    logger.info(f"Starting device configuration for {zone} zone")

    for device in devices[zone]:
        device_ip = device["ip"]
        config_commands = device["config"]

        try:
            logger.info(f"Connecting to device {device_ip}")
            connection = create_ssh_connection(device_ip)
            for command in config_commands:
                send_ssh_command(connection, command)
            close_ssh_connection(connection)
            logger.info(f"Configured device {device_ip}")
        except Exception as e:
            logger.error(f"Failed to configure device {device_ip}: {e}")

    logger.info(f"Completed device configuration for {zone} zone")
