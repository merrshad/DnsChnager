#!/bin/bash

# Ensure the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo."
  exit 1
fi

# Install colorama if not already installed
if ! python3 -c "import colorama" 2>/dev/null; then
  echo "Installing colorama..."
  pip3 install colorama
fi

# Copy the script to a system-wide executable path
cp dns.py /usr/local/bin/dns

# Grant execute permissions
chmod +x /usr/local/bin/dns

echo "myDNS has been successfully installed!"
echo "To connect: sudo dns -c"
echo "To disconnect: sudo dns -dc"
