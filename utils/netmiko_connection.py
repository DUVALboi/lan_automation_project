from netmiko import ConnectHandler
import logging

logger = logging.getLogger(__name__)

def create_connection(device):
    try:
        logger.info(f"Connecting to {device['ip']}")
        connection = ConnectHandler(**device)
        connection.enable()
        logger.info(f"Connected to {device['ip']}")
        return connection
    except Exception as e:
        logger.error(f"Failed to connect to {device['ip']}: {e}")
        return None

def send_commands(connection, commands):
    try:
        logger.info(f"Sending commands to {connection.host}")
        output = connection.send_config_set(commands)
        logger.info(f"Commands sent to {connection.host}")
        return output
    except Exception as e:
        logger.error(f"Failed to send commands to {connection.host}: {e}")
        return None

def save_configuration(connection):
    try:
        logger.info(f"Saving configuration on {connection.host}")
        connection.save_config()
        logger.info(f"Configuration saved on {connection.host}")
    except Exception as e:
        logger.error(f"Failed to save configuration on {connection.host}: {e}")

def close_connection(connection):
    try:
        logger.info(f"Closing connection to {connection.host}")
        connection.disconnect()
        logger.info(f"Connection closed to {connection.host}")
    except Exception as e:
        logger.error(f"Failed to close connection to {connection.host}: {e}")

# Example usage
if __name__ == "__main__":
    device = {
        "device_type": "cisco_ios",
        "ip": "192.168.1.1",
        "username": "admin",
        "password": "password",
        "secret": "secret",
    }
    commands = ["interface Gi1", "description Test"]
    conn = create_connection(device)
    if conn:
        send_commands(conn, commands)
        save_configuration(conn)
        close_connection(conn)
