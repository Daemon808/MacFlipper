# MAC Address Changer

This script allows you to change the MAC address of a specified network interface. It's useful for network testing, enhancing privacy, or troubleshooting connectivity issues.

## How It Works

The script does the following:
1. Takes the network interface and the new MAC address as input.
2. Disables the network interface.
3. Assigns the new MAC address.
4. Re-enables the network interface.
5. Verifies if the MAC address was successfully changed.

## Prerequisites

- Python 3.x
- Administrator/root privileges (required to change network settings)

## Usage

1. Clone the repository or download the script:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Run the script with the required options:
    ```bash
    python3 mac_changer.py -i <interface> -m <new_mac_address>
    ```

    Example:
    ```bash
    python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
    ```

## Options

- `-i, --interface` : The network interface you want to change the MAC address for (e.g., eth0, wlan0).
- `-m, --mac` : The new MAC address you want to set (e.g., 00:11:22:33:44:55).

## Important Notes

- Use this script responsibly. Changing your MAC address can have legal and ethical implications depending on the context.
- Ensure that the MAC address format is valid (e.g., `XX:XX:XX:XX:XX:XX`).