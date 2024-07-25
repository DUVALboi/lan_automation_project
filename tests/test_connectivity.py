import logging
from utils.ssh_connection import create_ssh_connection, send_ssh_command, close_ssh_connection

def test_connectivity(devices):
    """Test connectivity to devices."""
    logger = logging.getLogger("tests.test_connectivity")
    logger.info("Starting connectivity tests.")

    for zone, device_list in devices.items():
        logger.info(f"Testing connectivity for {zone} zone.")
        for device in device_list:
            try:
                conn = create_ssh_connection(device)
                output = send_ssh_command(conn, "ping 8.8.8.8")
                logger.info(f"Ping output for device {device['ip']}: {output}")
                close_ssh_connection(conn)
            except Exception as e:
                logger.error(f"Failed to connect to device {device['ip']}: {str(e)}")

    logger.info("Completed connectivity tests.")
