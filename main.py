import os
import scripts.automate_vlans as automate_vlans
import scripts.configure_devices as configure_devices
import scripts.configure_pcs as configure_pcs
from utils.logging_config import setup_logging
from utils.terminal_utils import clear_screen, display_menu, pause

def authenticate_user():
    """Authenticates the user."""
    expected_username = "279315"
    expected_password = "2d9!!0B3"

    clear_terminal()
    print_output("=== User Authentication ===")
    username = get_input("Enter username: ")
    password = get_input("Enter password: ")

    if username == expected_username and password == expected_password:
        print_output("Authentication successful!")
        logger.info("User authentication successful.")
        return True
    else:
        print_output("Authentication failed. Please try again.")
        logger.warning("User authentication failed.")
        return False

def main_menu():
    setup_logging()
    while True:
        clear_screen()
        choice = display_menu("Automation Interface", ["Automate VLANs", "Automate Devices", "Exit"])

        if choice == '1':
            vlan_menu()
        elif choice == '2':
            device_menu()
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

def vlan_menu():
    while True:
        clear_screen()
        
        choice = display_menu("Automate VLANs", ["Green Zone", "Yellow Zone", "Back"])

        if choice == '1':
            automate_vlans.automate_vlans("green")
        elif choice == '2':
            automate_vlans.automate_vlans("yellow")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def device_menu():
    while True:
        clear_screen()
        choice = display_menu("Automate Devices", ["Green Zone", "Yellow Zone", "Back"])

        if choice == '1':
            device_zone_menu("green")
        elif choice == '2':
            device_zone_menu("yellow")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def device_zone_menu(zone):
    while True:
        clear_screen()
        title = f"Automate {zone.capitalize()} Zone Devices"
        choice = display_menu(title, ["Automate PCs", "Automate Switches", "Back"])

        if choice == '1':
            configure_pcs.automate_pcs(zone)
            pause()
        elif choice == '2':
            configure_devices.automate_devices(zone)
            pause()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
