import paramiko
import logging

logger = logging.getLogger(__name__)

def create_ssh_connection(hostname, port, username, password):
    """Create an SSH connection to the network device."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)
        logger.info(f"Successfully connected to {hostname}")
        return ssh
    except Exception as e:
        logger.error(f"Failed to connect to {hostname}: {e}")
        return None

def send_ssh_command(ssh, command):
    """Send a command via SSH to the network device."""
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        logger.info(f"Successfully sent command to {ssh.get_transport().getpeername()[0]}")
        return output
    except Exception as e:
        logger.error(f"Failed to execute command on {ssh.get_transport().getpeername()[0]}: {e}")
        return None

def close_ssh_connection(ssh):
    """Close the SSH connection to the network device."""
    try:
        ssh.close()
        logger.info(f"Successfully disconnected from {ssh.get_transport().getpeername()[0]}")
    except Exception as e:
        logger.error(f"Failed to disconnect from {ssh.get_transport().getpeername()[0]}: {e}")

# Example usage
if __name__ == "__main__":
    device = {
        "hostname": "192.168.1.1",
        "port": 22,
        "username": "admin",
        "password": "password"
    }
    ssh = create_ssh_connection(device["hostname"], device["port"], device["username"], device["password"])
    if ssh:
        output = send_ssh_command(ssh, "show ip interface brief")
        print(output)
        close_ssh_connection(ssh)
