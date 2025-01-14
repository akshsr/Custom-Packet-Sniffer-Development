# DNS Packet Sniffer

This Python script captures and logs DNS queries by listening to UDP traffic on port 53. It extracts DNS query details such as the domain name and query type, as well as source and destination IP addresses. The captured information is logged in a file (`dns_queries.log`) and printed to the console for real-time monitoring.

## Features

- **Captures DNS packets**: Listens to raw UDP traffic on port 53 (DNS).
- **Extracts DNS query details**: Logs the domain name and query type (e.g., A, AAAA, MX).
- **Logs source and destination IP addresses**: Captures both sender and receiver IPs.
- **Real-time logging**: Outputs DNS queries to the console as they are captured.
- **Log storage**: Appends captured data into a log file (`dns_queries.log`).
- **Graceful exit**: Allows stopping the packet capture with `Ctrl+C`.

## Requirements

- Python 3.x
- **Privileges**: Root or administrator permissions are required to capture raw socket data.

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/akshsr/dns-packet-sniffer.git
    ```

2. Install necessary libraries (if not already installed):

    ```bash
    pip install socket
    ```

## Usage

1. Run the script with appropriate permissions (root or administrator):

    ```bash
    sudo python3 dns_packet_sniffer.py
    ```

2. The script will start capturing DNS packets and logging the results.

    - Example log format:

      ```
      2025-01-14 14:32:09 | Source IP: 192.168.1.1 | Destination IP: 8.8.8.8 | Domain: example.com | Type: 1
      ```

    - The script will display the following details:
      - **Timestamp**
      - **Source IP address**
      - **Destination IP address**
      - **Domain being queried**
      - **DNS query type** (e.g., 1 for A, 28 for AAAA)

3. To stop the packet capture, press `Ctrl+C`.

   The script will terminate gracefully, and the last few captured packets will be logged.

## Code Explanation

### `parse_dns_query(data)`
- This function parses the DNS query section of the packet, extracting the domain name and query type. It starts at byte 12 (after the DNS header) and decodes the domain name from the packet data.

### `parse_ip_header(packet)`
- This function extracts the source and destination IP addresses from the IP header of the packet. It uses the `struct` module to unpack the IP header and then converts the IP addresses into readable formats.

### `capture_dns_packets()`
- This function creates a raw socket to capture UDP packets. It listens for packets on port 53 (DNS), extracts the relevant information (IP addresses, domain names, and query types), and logs the data to both the console and a log file.

## Logging

- Logs are saved in a file named `dns_queries.log`.
- Each log entry contains the timestamp, source IP, destination IP, domain name, and query type.

## Notes

- **Root/Administrator access**: Capturing raw packets requires root or administrator privileges on most systems.
- **Port 53**: The script captures DNS queries, which typically use UDP on port 53. Ensure this port is not blocked or filtered on your network.

## Troubleshooting

- **No packets captured**: Ensure you have the necessary permissions (root/admin).
- **On Windows**: Raw sockets may require additional configuration. If you're on Windows, you might need to install WinPcap or use a tool like `npf` for packet capturing.

## License

This project is licensed under the MIT License.

---

Feel free to modify and extend the script as needed.
