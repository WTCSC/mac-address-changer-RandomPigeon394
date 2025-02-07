#!/bin/bash

# First we need a function to print our usage instructions
usage() {
    echo "Usage: $0 -i <interface> -m <mac_address>"
    echo "Options:"
    echo "  -i    Network interface (e.g., eth0, wlan0)"
    echo "  -m    New MAC address to assign (format: XX:XX:XX:XX:XX:XX)"
    exit 1
}

# Next we confirm the MAC address format
validate_mac() {
    if [[ $1 =~ ^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$ ]]; then
        return 0
    else
        echo "Error: Invalid MAC address format."
        exit 1
    fi
}

# Next we use the trap command if there are any errors while executing then it will let us know 
trap 'echo "An error occurred. Exiting..."; exit 1' ERR

# Next we use the information typed by the user to run the script
while getopts "i:m:" opt; do
    case $opt in
        i) INTERFACE=$OPTARG ;;
        m) MAC_ADDRESS=$OPTARG ;;
        *) usage ;;
    esac
done

# This part makes sure the user inputed everything correctly 
if [[ -z $INTERFACE || -z $MAC_ADDRESS ]]; then
    usage
fi

# Confirm the MAC address format
validate_mac $MAC_ADDRESS

# Now we change the MAC address using the ip command
ip link set $INTERFACE down || { echo "Error: Failed to bring down the interface $INTERFACE."; exit 1; }
ip link set $INTERFACE address $MAC_ADDRESS || { echo "Error: Failed to set MAC address."; exit 1; }
ip link set $INTERFACE up || { echo "Error: Failed to bring up the interface $INTERFACE."; exit 1; }

# And last but not least we show a success message to let the user know its changed
echo "Successfully changed MAC address of $INTERFACE to $MAC_ADDRESS."
