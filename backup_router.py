from netmiko import ConnectHandler
from datetime import datetime
import os

# 1. Define the connection details for Cisco DevNet Sandbox
# These are public lab routers provided by Cisco
cisco_sandbox = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-recommends.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,
}

print(f"Connecting to {cisco_sandbox['host']}...")

# 2. Establish the connection
try:
    net_connect = ConnectHandler(**cisco_sandbox)
    net_connect.enable() # Enter enable mode
    
    # Get the hostname to make the filename pretty
    hostname = net_connect.find_prompt().replace('#', '')
    print(f"Connected to: {hostname}")

    # 3. Send the command
    print("Pulling running configuration...")
    output = net_connect.send_command('show running-config')

    # 4. Save to file
    now = datetime.now()
    # Create a cleaner timestamp (Year-Month-Day_Hour-Minute)
    timestamp = now.strftime("%Y-%m-%d_%H-%M")
    filename = f"{hostname}_backup_{timestamp}.txt"

    with open(filename, 'w') as backup_file:
        backup_file.write(output)
    
    print(f"SUCCESS! Configuration saved to: {filename}")
    
    # 5. Disconnect
    net_connect.disconnect()

except Exception as e:
    print(f"Failed to connect: {e}")
