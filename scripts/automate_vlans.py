# scripts/automate_vlans.py

from utils.ssh_connection import create_ssh_connection, send_ssh_command, close_ssh_connection
from config.device_config import devices

def assign_access_vlan():
    while True:
        print("\nAssign Access VLAN")
        print("Select a switch:")
        for i, device_name in enumerate(devices.keys(), 1):
            print(f"{i}. {device_name}")
        print("0. Back")
        
        switch_number = int(input("Enter switch number: "))
        if switch_number == 0:
            return  # Go back to the main menu

        selected_switch = list(devices.keys())[switch_number - 1]

        connection = create_ssh_connection(devices[selected_switch])

        while True:
            # Fetch interface list from the device
            interface_command = "show ip interface brief"
            output = send_ssh_command(connection, interface_command)
            print("\nAvailable interfaces:")

            # Define interfaces based on the selected switch, excluding specific interfaces as needed
            if selected_switch == "Switch_2_Yellow":
                interfaces = ['GigabitEthernet1/3']  # Exclude GigabitEthernet1/2 since it connects to Server_Rack
            else:
                interfaces = ['GigabitEthernet1/2', 'GigabitEthernet1/3']  # Add more interfaces as needed

            for i, interface in enumerate(interfaces, 1):
                print(f"{i}. {interface}")
            print("0. Back")
            
            interface_number = int(input("Select an interface: "))
            if interface_number == 0:
                break  # Go back to the switch selection menu
            
            selected_interface = interfaces[interface_number - 1]

            vlan = input("Enter VLAN (10, 20, or 30) or 'back' to go back: ")
            if vlan.lower() == "back":
                continue  # Go back to the interface selection menu

            # Constructing the configuration commands
            commands = [
                f"interface {selected_interface}",
                f"switchport access vlan {vlan}",
                "switchport mode access",
                "exit"
            ]

            # Sending the configuration commands to the device
            connection.send_config_set(commands)  # Correct method name

            print(f"VLAN {vlan} has been assigned to {selected_interface} on {selected_switch}.")
            break  # After successful configuration, go back to the switch selection menu

        close_ssh_connection(connection)

