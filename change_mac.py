import re
import argparse
import subprocess
import sys

# Function to display instructions
def usage():
    print("Usage: change_mac.py -i <interface> -m <mac_address>")
    print("Options:")
    print("  -i    Network interface (e.g., eth0, wlan0)")
    print("  -m    New MAC address to assign (format: XX:XX:XX:XX:XX:XX)")
    sys.exit(1)

# Function to see if the given MAC address follows the right format
def validate_mac(mac):
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$" 
    if not re.match(pattern, mac):
        print("Error: Invalid MAC address format.")
        sys.exit(1)

# Function to change the MAC address of the given interface
def change_mac(interface, mac_address):
    try:
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)  # Disable the network interface
        subprocess.run(["ip", "link", "set", interface, "address", mac_address], check=True)  # Change the MAC address
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)  # Enable the network interface again
        print(f"Successfully changed MAC address of {interface} to {mac_address}.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to change MAC address on {interface}.")
        sys.exit(1)

# Main function to handle command-line arguments and execute the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change MAC Address")  # Create an argument parser
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")  # Argument for network interface
    parser.add_argument("-m", "--mac", required=True, help="New MAC address (format: XX:XX:XX:XX:XX:XX)")  # Argument for new MAC address
    args = parser.parse_args()

    validate_mac(args.mac)  # Change the given MAC address
    change_mac(args.interface, args.mac)  # Last it tries to change the MAC address
