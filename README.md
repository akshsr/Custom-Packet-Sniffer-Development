# Custom-Packet-Sniffer-Development
Python script to sniff the network packets


DNS Packet Sniffer
This Python script captures and logs DNS queries by listening to UDP traffic on port 53. It extracts DNS query details such as the domain name and query type, as well as source and destination IP addresses. The captured information is logged in a file (dns_queries.log) and printed to the console for real-time monitoring.

Features
Captures DNS packets: Listens to raw UDP traffic on port 53 (DNS).
Extracts DNS query details: Logs the domain name and query type (e.g., A, AAAA, MX).
Logs source and destination IP addresses: Captures both sender and receiver IPs.
Real-time logging: Outputs DNS queries to the console as they are captured.
Log storage: Appends captured data into a log file (dns_queries.log).
Graceful exit: Allows stopping the packet capture with Ctrl+C.
