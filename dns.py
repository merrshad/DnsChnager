#!/usr/bin/env python3
import os
import sys
import subprocess
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# List of DNS servers to use
DNS_SERVERS = ["178.22.122.100", "185.51.200.2"]  # Your DNS servers
RESOLV_CONF = "/etc/resolv.conf"
BACKUP_FILE = "/etc/resolv.conf.backup"

def connect_dns():
    """Set custom DNS servers by modifying /etc/resolv.conf"""
    if not os.geteuid() == 0:
        print(f"{Fore.RED}Please run the program with root privileges (e.g., using sudo).{Style.RESET_ALL}")
        sys.exit(1)

    # Backup the current resolv.conf
    if os.path.exists(RESOLV_CONF):
        try:
            subprocess.run(["cp", RESOLV_CONF, BACKUP_FILE], check=True)
            print(f"{Fore.YELLOW}Backed up current DNS settings to {BACKUP_FILE}{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error backing up {RESOLV_CONF}: {e}{Style.RESET_ALL}")
            sys.exit(1)

    # Write new DNS servers to resolv.conf
    try:
        with open(RESOLV_CONF, "w") as f:
            for dns in DNS_SERVERS:
                f.write(f"nameserver {dns}\n")
        print(f"{Fore.GREEN}DNS servers successfully set:{Style.RESET_ALL} {DNS_SERVERS}")
    except IOError as e:
        print(f"{Fore.RED}Error writing to {RESOLV_CONF}: {e}{Style.RESET_ALL}")
        sys.exit(1)

def disconnect_dns():
    """Restore the original DNS settings from backup"""
    if not os.geteuid() == 0:
        print(f"{Fore.RED}Please run the program with root privileges (e.g., using sudo).{Style.RESET_ALL}")
        sys.exit(1)

    # Restore the backup if it exists
    if os.path.exists(BACKUP_FILE):
        try:
            subprocess.run(["mv", BACKUP_FILE, RESOLV_CONF], check=True)
            print(f"{Fore.YELLOW}DNS servers disconnected and restored from backup.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error restoring {RESOLV_CONF}: {e}{Style.RESET_ALL}")
            sys.exit(1)
    else:
        # If no backup exists, clear resolv.conf
        try:
            with open(RESOLV_CONF, "w") as f:
                f.write("")
            print(f"{Fore.YELLOW}DNS servers disconnected (no backup found, cleared {RESOLV_CONF}).{Style.RESET_ALL}")
        except IOError as e:
            print(f"{Fore.RED}Error clearing {RESOLV_CONF}: {e}{Style.RESET_ALL}")
            sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.CYAN}Usage: dns [-c | -dc]{Style.RESET_ALL}")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-c":
        connect_dns()
    elif command == "-dc":
        disconnect_dns()
    else:
        print(f"{Fore.RED}Invalid argument. Use '-c' to connect or '-dc' to disconnect.{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
