# Cisco IOS Configuration Auto-Backup

## Project Overview
This Python automation script streamlines the daily operations of network administration. It utilizes the **Netmiko** library to establish secure SSH connections to Cisco IOS devices, capture the `running-config`, and save it locally with a timestamp.

## Key Features
* **Automated SSH Handling:** Uses Netmiko to handle SSH handshake and privilege escalation.
* **Error Handling:** Includes try/except blocks to manage connection timeouts or authentication failures.
* **Dynamic File Naming:** Automatically names backup files based on the device hostname and current timestamp.

## Technologies Used
* Python 3.x
* Netmiko (SSH Library)
* Cisco IOS / IOS XE

## How to Run
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the script:
   `python backup_router.py`

## Project Status
Tested and verified against **Cisco DevNet Sandbox (IOS XE)** environments.
