from utils.ssh_connection import create_ssh_connection, send_ssh_command, close_ssh_connection
from config.device_config import devices

def automate_devices(zone):
    for device in devices[zone]:
        client = create_ssh_connection(device['hostname'], device['username'], device['password'])
        if client:
            for command in device['commands']:
                output = send_ssh_command(client, command)
                print(output)
            close_ssh_connection(client)

if __name__ == "__main__":
    zone = input("Enter zone (green/yellow): ").strip().lower()
    automate_devices(zone)
