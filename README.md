# LAN Automation Project

This project automates the configuration of a Local Area Network (LAN) using Python scripts and network libraries such as Paramiko and Netmiko.

## Project Structure

- `config/`: Configuration files for devices and VLANs.
- `logs/`: Logs of the automation process.
- `scripts/`: Main automation scripts.
- `tests/`: Test scripts for verifying configurations.
- `utils/`: Utility scripts for SSH connections.
- `main.py`: Main entry point for running the automation.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## Setup

1. Install Python (if not already installed).
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt

## Usage

Upon running 'main.py' on the `Server_Rack` PC, the script prompts the user to log in with the admin credentials.
After successful authentication, the user can choose from the four options which are configuring the devices, automating the VLANs, testing the connectivity or, exiting.
Chosing either to configure the devices or the VLANs, the admin will be prompted to choose either the Green or Yellow Zones.
In the Configure the Devices option, after chosing one of the zones, the user will have to chose to configure either the switches or the PCs.
In the Configure VLANs option, the program will configure the VLAN interfaces on the switches.
The automation process logs all activities in the 'logs/automation.log' file for preview and debugging.

## Configuration Files

- `config/device_config.py`: Contains device configuration details such as IP addresses and authentication information.
- `config/vlans_config.py`: Defines VLAN configurations including VLAN IDs, name, and devices assigned to each VLAN.

## Scripts

- `scripts/configure_devices.py`: Automates the configuration of network devices using Netmiko.
- `scripts/automate_vlans.py`: Automates VLAN setup on the network devices(switches).

## Utilities

- `utils/logging_config.py`: Configures logging to record automation activities in logs/automation.log.
- `utils/netmiko_connection.py`: Handles network device connections using Netmiko.
- `utils/ssh_connection.py`: Manages SSH connections to devices using Paramiko.
- `utils/terminal_utils.py`: Provides terminal utility functions for user interaction.

## Tests

- `tests/test_connectivity.py`: Scripts to test network connectivity.
- `tests/test_vlans.py`: Scripts to test VLAN configurations.

## GNS3

- 'http://ensa1-gns3.savnet.ro/static/web-ui/server/1/projects'
- Open the link and look for 'MariaSebastian_BCThesis'
- The code is stored in 'AAA-1' in the 'Blue Zone' and in 'Server_Rack' in the 'Yellow Zone'.
