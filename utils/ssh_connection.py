# utils/ssh_connection.py

from netmiko import ConnectHandler

class SSHConnection:
    def __init__(self, device_params):
        self.device_params = device_params
        self.connection = None

    def connect(self):
        try:
            self.connection = ConnectHandler(**self.device_params)
            print(f"Connected to {self.device_params['ip']}")
        except Exception as e:
            print(f"Failed to connect to {self.device_params['ip']}: {str(e)}")

    def send_command(self, command):
        if self.connection:
            return self.connection.send_command(command)
        else:
            print("Connection not established.")

    def send_config_set(self, config_commands):
        if self.connection:
            return self.connection.send_config_set(config_commands)
        else:
            print("Connection not established.")

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()
            print(f"Disconnected from {self.device_params['ip']}")
        else:
            print("No connection to disconnect.")

# Functions that the script might try to import
def create_ssh_connection(device_params):
    ssh_conn = SSHConnection(device_params)
    ssh_conn.connect()
    return ssh_conn

def send_ssh_command(ssh_conn, command):
    return ssh_conn.send_command(command)

def close_ssh_connection(ssh_conn):
    ssh_conn.disconnect()
