import logging
from utils.netmiko_connection import create_connection, send_commands, save_configuration, close_connection
from config.vlans_config import vlans

logger = logging.getLogger(__name__)

def automate_vlans(zone):
    """Automate VLAN configuration for the given zone."""
    logger.info(f"Starting VLAN automation for {zone} zone")
    
    for vlan in vlans[zone]:
        vlan_id = vlan["id"]
        vlan_name = vlan["name"]
        logger.info(f"Configuring VLAN {vlan_id} - {vlan_name}")

        for device_ip in vlan["devices"]:
            try:
                logger.info(f"Connecting to device {device_ip}")
                conn = create_connection(device_ip)
                commands = [
                    f"vlan {vlan_id}",
                    f"name {vlan_name}",
                    "exit"
                ]
                send_commands(conn, commands)
                save_configuration(conn)
                close_connection(conn)
                logger.info(f"Successfully configured VLAN {vlan_id} on device {device_ip}")
            except Exception as e:
                logger.error(f"Failed to configure VLAN {vlan_id} on device {device_ip}: {e}")

    logger.info(f"Completed VLAN automation for {zone} zone")
