# Firewall Management Script

This Python script provides a simple command-line interface (CLI) for managing Windows Firewall rules using PowerShell commands. It allows users to list existing firewall rules, add new rules, and delete existing rules.

## Features

- **List Firewall Rules**: Displays all the current firewall rules with details such as name, display name, enabled status, direction, action, profile, local and remote ports, addresses, protocol, program, and service.
- **Add Firewall Rule**: Allows adding a new firewall rule with specified details like name, direction, action, protocol, and local port.
- **Delete Firewall Rule**: Enables the deletion of an existing firewall rule by its name.

## Requirements

- Windows operating system
- Python 3.x
- PowerShell

## Usage

1. **List Firewall Rules**
   - Run the script and select option `1` to list all the current firewall rules.

2. **Add a New Firewall Rule**
   - Select option `2` and follow the prompts to enter the rule name, direction (Inbound/Outbound), action (Allow/Block), protocol (TCP/UDP), and local port.

3. **Delete a Firewall Rule**
   - Choose option `3` and enter the name of the rule you wish to delete.

4. **Exit**
   - Select option `4` to exit the script.

## Running the Script

To run the script, navigate to the directory containing `firewall.py` and execute the following command in your terminal:

```bash
python firewall.py
