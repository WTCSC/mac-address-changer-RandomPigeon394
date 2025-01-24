MAC Address Changer Script

Overview
This script allows you to change the MAC address of your network interface (like your Wifi or ethernet).
A MAC address is a identity for your device and you can change it for whatever reason like maybe for privacy.

How do I run the script???
Step 1: Open the terminal
Youll have to run the script in your terminal for it to work
Step 2: Make the script able to run
Next you need to give it permission to run so make sure to type: chmod +x code.sh
Step 3: Run the script!
./mac_changer.sh -i <interface> -m <new_mac_address>
Replace <interface> with your network interface name
Replace <new_mac_address> with the MAC address you want in the format 00:00:00:00:00:00
Example: ./mac_changer.sh -i enp0s3 -m 00:11:22:33:44:55
Step 4: Done!
Once you run the script correctly you should see a success message after

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tp86o73G)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17833455)
