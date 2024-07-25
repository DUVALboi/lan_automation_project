import os
import sys
import time
from getpass import getpass
from utils.logging_config import setup_logging
from utils.terminal_utils import display_menu, clear_screen
import scripts.automate_vlans as automate_vlans
import scripts.configure_devices as configure_devices
import scripts.configure_pcs as configure_pcs
import tests.test_connectivity as test_connectivity

# Setup logging
setup_logging()

# Authentication function
def authenticate():
    clear_screen()
    print("Authenticate the user")
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    if username == "admin" and password == "automation":
        print("Authentication successful.")
        time.sleep(1)
        return True
    else:
        print("Authentication failed. Exiting...")
        time.sleep(1)
        sys.exit(1)

# VLAN automation menu
def vlan_menu():
    while True:
        choice = display_menu("Automate VLAN", ["Green Zone", "Yellow Zone", "Back"])
        if choice == "1":
            automate_vlans.automate_vlans("green")
        elif choice == "2":
            automate_vlans.automate_vlans("yellow")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
            time.sleep(1)

# Device automation menu
def device_menu():
    while True:
        choice = display_menu("Automate Devices", ["Green Zone", "Yellow Zone", "Back"])
        if choice == "1":
            zone_choice = display_menu("Automate Green Zone Devices", ["Automate PCs", "Automate Switches", "Back"])
            if zone_choice == "1":
                configure_pcs.configure_pcs("green")
            elif zone_choice == "2":
                configure_devices.configure_devices("green")
            elif zone_choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
                time.sleep(1)
        elif choice == "2":
            zone_choice = display_menu("Automate Yellow Zone Devices", ["Automate PCs", "Automate Switches", "Back"])
            if zone_choice == "1":
                configure_pcs.configure_pcs("yellow")
            elif zone_choice == "2":
                configure_devices.configure_devices("yellow")
            elif zone_choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
                time.sleep(1)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
            time.sleep(1)

# Main menu
def main_menu():
    devices = {
        "green": [
            {"device_type": "cisco_ios", "ip": "192.168.99.2", "username": "admin", "password": "password"},
            {"device_type": "cisco_ios", "ip": "192.168.99.3", "username": "admin", "password": "password"},
            {"device_type": "cisco_ios", "ip": "192.168.99.4", "username": "admin", "password": "password"},
            {"device_type": "cisco_ios", "ip": "192.168.99.5", "username": "admin", "password": "password"},
        ],
        "yellow": [
            {"device_type": "cisco_ios", "ip": "192.169.98.1", "username": "admin", "password": "password"},
            {"device_type": "cisco_ios", "ip": "192.169.98.2", "username": "admin", "password": "password"},
            {"device_type": "cisco_ios", "ip": "192.169.98.3", "username": "admin", "password": "password"},
        ]
    }

    while True:
        choice = display_menu("Main Menu", ["Automate VLANs", "Automate Devices", "Test Connectivity", "Exit"])
        if choice == "1":
            vlan_menu()
        elif choice == "2":
            device_menu()
        elif choice == "3":
            test_connectivity.test_connectivity(devices)
        elif choice == "4":
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")
            time.sleep(1)

if __name__ == "__main__":
    authenticate()
    main_menu()
