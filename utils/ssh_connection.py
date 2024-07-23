import paramiko
import logging

logger = logging.getLogger(__name__)

def create_ssh_connection(hostname, username, password):
    try:
        logger.info(f"Connecting to {hostname}")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        logger.info(f"Connected to {hostname}")
        return client
    except Exception as e:
        logger.error(f"Failed to connect to {hostname}: {e}")
        return None

def send_ssh_command(client, command):
    try:
        logger.info(f"Sending command to {client.get_transport().getpeername()[0]}")
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        logger.info(f"Command sent to {client.get_transport().getpeername()[0]}")
        return output
    except Exception as e:
        logger.error(f"Failed to send command: {e}")
        return None

def close_ssh_connection(client):
    try:
        logger.info(f"Closing connection to {client.get_transport().getpeername()[0]}")
        client.close()
        logger.info(f"Connection closed")
    except Exception as e:
        logger.error(f"Failed to close connection: {e}")

# Example usage
if __name__ == "__main__":
    hostname = "192.168.1.1"
    username = "admin"
    password = "password"
    command = "show running-config"
    
    client = create_ssh_connection(hostname, username, password)
    if client:
        output = send_ssh_command(client, command)
        print(output)
        close_ssh_connection(client)
