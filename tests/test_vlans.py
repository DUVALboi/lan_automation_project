import logging
from config.vlans_config import vlans
from utils.netmiko_connection import create_connection, send_commands, close_connection

logger = logging.getLogger(__name__)

def verify_vlan(device, vlan_id):
    """Verify that a VLAN exists on a device."""
    commands = [f"show vlan id {vlan_id}"]
    output = send_commands(device, commands)
    if f"VLAN {vlan_id}" in output:
        logger.info(f"VLAN {vlan_id} exists on {device['ip']}")
        return True
    else:
        logger.error(f"VLAN {vlan_id} does not exist on {device['ip']}")
        return False

def verify_vlans(zone):
    """Verify VLAN configurations on all devices in a specified zone."""
    logger.info(f"Starting VLAN verification for {zone} zone")

    for vlan in vlans[zone]:
        for device_ip in vlan["devices"]:
            device = {
                "device_type": "cisco_ios",
                "ip": device_ip,
                "username": "admin",
                "password": "automation",
                "secret": "automation",
            }
            connection = create_connection(device)
            if connection:
                if verify_vlan(device, vlan["id"]):
                    logger.info(f"VLAN {vlan['id']} verified on {device_ip}")
                else:
                    logger.error(f"Failed to verify VLAN {vlan['id']} on {device_ip}")
                close_connection(connection)
            else:
                logger.error(f"Failed to connect to {device_ip}")

    logger.info(f"Completed VLAN verification for {zone} zone")

if __name__ == "__main__":
    zone = input("Enter the zone to verify (green/yellow): ").strip().lower()
    if zone in vlans:
        verify_vlans(zone)
    else:
        print(f"Invalid zone: {zone}. Valid options are: {', '.join(vlans.keys())}")
