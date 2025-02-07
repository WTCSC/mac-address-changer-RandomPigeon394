# MAC Address Changer Script

## Overview
This script allows you to change the MAC address of your network interface (like your Wifi or ethernet).
A MAC address is a identity for your device and you can change it for whatever reason like maybe for privacy.

## How do I run the script???
### Step 1: Open the terminal
Youll have to run the script in your terminal for it to work
### Step 2: Make the script able to run
Next you need to give it permission to run so make sure to type: chmod +x code.sh
### Step 3: Run the script!
./mac_changer.sh -i <interface> -m <new_mac_address>
Replace <interface> with your network interface name
Replace <new_mac_address> with the MAC address you want in the format 00:00:00:00:00:00
Example: ./mac_changer.sh -i enp0s3 -m 00:11:22:33:44:55
### Step 4: Done!
Once you run the script correctly you should see a success message after

# How to run the code in python?
### Step 1
To run the code in python it is very similar first open the terminal 
### Step 2
The code to run the script is: sudo python3 change_mac.py -i <interface> -m <new_mac_address>
Now you can change the MAC address to whatever you want. 
An example of a working code would be: sudo python3 change_mac.py -i enp0s3 -m 00:1A:2B:3C:4D:5E
### Step 4
Now you should be finsihed and should get the code saying "Successfully changed MAC address of <interface> to <new_mac_address>"
