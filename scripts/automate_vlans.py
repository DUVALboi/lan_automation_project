from utils.netmiko_connection import create_connection, send_commands, save_configuration, close_connection
from config.vlans_config import vlans

def automate_vlans(zone):
    for vlan in vlans[zone]:
        for device_ip in vlan['devices']:
            device = {
                "device_type": "cisco_ios",
                "ip": device_ip,
                "username": "admin",
                "password": "password",
                "secret": "secret",
            }
            connection = create_connection(device)
            if connection:
                commands = [
                    f"vlan {vlan['id']}",
                    f"name {vlan['name']}"
                ]
                output = send_commands(connection, commands)
                print(output)
                save_configuration(connection)
                close_connection(connection)

if __name__ == "__main__":
    zone = input("Enter zone (green/yellow): ").strip().lower()
    automate_vlans(zone)
