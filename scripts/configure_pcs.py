import logging
from utils.ssh_connection import create_ssh_connection, send_ssh_command, close_ssh_connection
from config.device_config import devices

logger = logging.getLogger(__name__)

def configure_pcs(zone):
    """Automate PC configuration for a specified zone."""
    logger.info(f"Starting PC configuration for {zone} zone")

    for device in devices[zone]:
        device_ip = device["ip"]
        config_commands = device["config"]

        try:
            logger.info(f"Connecting to PC {device_ip}")
            connection = create_ssh_connection(device_ip)
            for command in config_commands:
                send_ssh_command(connection, command)
            close_ssh_connection(connection)
            logger.info(f"Configured PC {device_ip}")
        except Exception as e:
            logger.error(f"Failed to configure PC {device_ip}: {e}")

    logger.info(f"Completed PC configuration for {zone} zone")
