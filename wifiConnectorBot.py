             #### Automatic Wifi Connector Bot ####
             
# Author : Punit Choudhary
# GitHub : Punit-Choudhary

# ** Steps followed in this Project **
# 1> Check for the Saved networks
# 2> Check for available networks
# 3> Asks user which saved network he want to connect
# 4> Disconnect the currently connected network
# 5> Checks whether preferred network is saved, if not than end the Program
# 6> if it is in saved network devices then check whether it is available or not
# 7> If it is available, then connect to the Preferred network


# Netsh : it is a CMD scripting utility which allows us to display or modify the network configuration of a computer

# Step 1 :
import os
import sys  # sys provides functions and variables used to manipulate different parts of the Python Runtime Environment.

saved_networks = os.popen('netsh wlan show profiles').read() # saved_networks contains all saved profiles/networks
#  popen opens a pipe to or from command. The return value is an open file object connected to the pipe,
# which can be read or written

print('Networks saved in your device are :' + saved_networks)

# Step 2 :

available_networks = os.popen('netsh wlan show networks').read()
print('Availble networks are ' + available_networks)

# Step 3 :
preferred_ssid = input('Enter the preferred Wifi SSID for your connection : ')

# Step 4 :
disconnect = os.popen('netsh wlan disconnect').read()
print(disconnect)

# Step 5 :
if preferred_ssid not in saved_networks:
    print('Profile for ' + preferred_ssid + " is not saved in system")
    print("Sorry, can't establish connection")
    sys.exit()
#Step 6 :
else:
    print("Profile for " + preferred_ssid + " is saved in system")
    while True:
        avail = os.popen('netsh wlan show networks').read()
        print("****** Searching for Network ******")
        if preferred_ssid in avail:
            print('Found')
            break
        
    print("--------------- Connecting ---------------")
    connecting = os.popen('netsh wlan connect name=' + '"' + preferred_ssid + '"').read()
    print(connecting)

