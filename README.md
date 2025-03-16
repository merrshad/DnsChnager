# DnsChnager

markdown
# myDNS - A Simple DNS Switcher for Linux

`myDNS` is a lightweight Python script designed to quickly switch DNS servers on Linux systems. It allows you to set custom DNS servers with a single command and revert to the system's default settings when you're done. This tool is particularly useful for users who need to temporarily change DNS servers for testing, privacy, or bypassing restrictions.

## Features
- Set custom DNS servers (e.g., `178.22.122.100`, `185.51.200.2`) with one command.
- Revert to the original DNS settings or clear them easily.
- Colorful terminal output for better readability using `colorama`.
- Simple installation and usage via the command line.

## Requirements
- **Linux**: Tested on systems with or without `systemd-resolved`.
- **Python 3**: Ensure Python 3.x is installed (`python3 --version`).
- **colorama**: A Python library for colored terminal output (installed automatically during setup).
- **Root Privileges**: Required to modify DNS settings (`sudo`).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/myDNS.git
   cd myDNS

    Run the Install Script:
    bash

    chmod +x install.sh
    sudo ./install.sh
    This will:
        Install the colorama library if not already present.
        Copy myDNS.py to /usr/local/bin/myDNS for global access.

## Usage

Run the following commands from any terminal directory:

sudo myDNS -c

    Sets the DNS servers defined in the script (e.g., 178.22.122.100, 185.51.200.2).
    Output will be in green if successful.

Revert to Default DNS:
sudo myDNS -dc

    Restores the original DNS settings from a backup or clears them if no backup exists.
    Output will be in yellow.

Check DNS Settings:

    cat /etc/resolv.conf

## Customization

To use different DNS servers:

    Open myDNS.py:
    
sudo nano /usr/local/bin/myDNS
Edit the DNS_SERVERS list:
python

    DNS_SERVERS = ["1.1.1.1", "1.0.0.1"]  # Example: Cloudflare DNS
    Save and exit (Ctrl+O, Enter, Ctrl+X).

## How It Works

    Connecting: Backs up the current /etc/resolv.conf and writes the custom DNS servers.
    Disconnecting: Restores the backup or clears /etc/resolv.conf if no backup is found.
    Note: If your system uses systemd-resolved, it might overwrite /etc/resolv.conf after a while. Stop the service temporarily if needed:
    bash

    sudo systemctl stop systemd-resolved

## Uninstallation

To remove myDNS:
bash
sudo rm /usr/local/bin/myDNS

Optionally, uninstall colorama if you no longer need it:
bash
sudo pip3 uninstall colorama
## Troubleshooting

    Permission Denied: Ensure you run commands with sudo.
    No Color Output: Verify colorama is installed (pip3 show colorama).
    DNS Not Applying: Check if systemd-resolved is active (systemctl status systemd-resolved) and stop it if necessary.
