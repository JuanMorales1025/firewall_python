import sys
import subprocess

def run_command(command):
    # Prefix the command to run it in PowerShell
    ps_command = f"powershell -Command \"{command}\""
    try:
        process = subprocess.Popen(ps_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()

        # Try decoding with utf-8, fall back to cp850 on failure
        try:
            stdout_decoded = stdout.decode('utf-8').strip() if stdout else ''
        except UnicodeDecodeError:
            stdout_decoded = stdout.decode('cp850').strip() if stdout else ''

        try:
            stderr_decoded = stderr.decode('utf-8').strip() if stderr else ''
        except UnicodeDecodeError:
            stderr_decoded = stderr.decode('cp850').strip() if stderr else ''

        return stdout_decoded, stderr_decoded
    except Exception as e:
        return '', str(e)

def list_rules():
    print("Listing current Firewall rules...")
    rules = run_command("Get-NetFirewallRule | Select-Object -Property Name, DisplayName, Enabled, Direction, Action, Profile, LocalPort, RemotePort, LocalAddress, RemoteAddress, Protocol, Program, Service | Format-Table -AutoSize")
    print(rules)


def add_rule(name, direction, action,protocol,localport):
    print(f"Adding new Firewall rule: {name}...")
    command = f"New-NetFirewallRule -DisplayName '{name}' -Direction {direction} -Action {action} -Protocol {protocol} -LocalPort {localport}"
    run_command(command)
    print("Rule added successfully!")

def delete_rule(name):
    print(f"Deleting Firewall rule: {name}")
    command = f"Remove-NetFirewallRule -DisplayName '{name}'"
    result, error = run_command(command)
    if error:
        print(f"Error deleting rule: {error}")
    else:
        print("Rule deleted successfully!")

def print_menu():
    print("1. List Firewall rules")
    print("2. Add new Firewall rule")
    print("3. Delete Firewall rule")
    print("4. Exit")

while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        list_rules()
    elif choice == "2":
        name = input("Enter the rule name: ")
        direction = input("Enter the direction (Inbound/Outbound): ")
        action = input("Enter the action (Allow/Block): ")
        protocol = input("Enter the protocol (TCP/UDP): ")
        localport = input("Enter the local port: ")
        add_rule(name, direction, action, protocol, localport)
    elif choice == "3":
        name = input("Enter rule name: ")
        delete_rule(name)
    elif choice == "4":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice!.\n Please try again.")