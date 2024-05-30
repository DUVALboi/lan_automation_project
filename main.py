# main.py
import getpass

import maskpass

from scripts.configure_devices import configure_devices
from scripts.automate_vlans import automate_vlans
from utils.logging_config import configure_logging, logger
from utils.terminal_utils import clear_terminal, get_input, print_output, exit_program

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
    """Displays the main menu."""
    clear_terminal()
    print_output("=== LAN Automation ===")
    print_output("1. Configure Devices")
    print_output("2. Automate VLANs")
    print_output("3. Exit")
    choice = get_input("Enter your choice: ")
    return choice

def main():
    """Main entry point of the program."""
    configure_logging()
    logger = configure_logging()

    authenticated = False
    while not authenticated:
        authenticated = authenticate_user()

    while True:
        choice = main_menu()

        if choice == '1':
            clear_terminal()
            print_output("=== Configure Devices ===")
            configure_devices()
            get_input("Press Enter to return to the main menu...")

        elif choice == '2':
            clear_terminal()
            print_output("=== Automate VLANs ===")
            automate_vlans()
            get_input("Press Enter to return to the main menu...")

        elif choice == '3':
            clear_terminal()
            print_output("Exiting...")
            logger.info("User exited the program.")
            exit_program()

        else:
            print_output("Invalid choice. Please try again.")
            logger.warning("User made an invalid choice.")

if __name__ == "__main__":
    main()
