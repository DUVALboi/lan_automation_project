# main.py

from scripts.automate_vlans import assign_access_vlan
from scripts.configure_pcs import assign_device_ips

def main_menu():
    while True:
        print("\nNetwork Automation Tool")
        print("1. Assign Access VLAN")
        print("2. Assign End Device IPs")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            assign_access_vlan()
        elif choice == '2':
            assign_device_ips()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
