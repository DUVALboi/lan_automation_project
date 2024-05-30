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

Upon running 'main.py', the script prompts the user to log in with the admin credentials.
After successful authentication, the user can choose from the two options(so far) which are configuring the devices or automating the VLANs.
The automation process logs all activities in the 'logs/automation.log' file for preview and debugging.

## Configuration Files

- `config/device_config.py`: Contains device configuration details such as IP addresses, authentication information, and commands to be executed on each device.
- `config/vlans_config.py`: Defines VLAN configurations including VLAN IDs, associated subnets, and devices assigned to each VLAN.

## Scripts

- `scripts/configure_devices.py`: Automates the configuration of network devices using Netmiko.
- `scripts/automate_vlans.py`: Automates VLAN setup on the network devices.

## Utilities

- `utils/logging_config.py`: Configures logging to record automation activities in logs/automation.log.
- `utils/netmiko_connection.py`: Handles network device connections using Netmiko.
- `utils/ssh_connection.py`: Manages SSH connections to devices using Paramiko.
- `utils/terminal_utils.py`: Provides terminal utility functions for user interaction.

## Future

This remains to be implemented inside the GNS3's virtual machine.