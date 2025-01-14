#!/bin/python3

import socket 
import struct 
import time 

def parse_dns_query(data):
	query_start = 12
	domain_name = ''
	
	while True:
		length = data[query_start]
		query_start += 1
		if length == 0:
			break
		domain_name += data[query_start:query_start + length].decode() + '.'
		query_start += length
	domain_name = domain_name[:-1]
	query_type = struct.unpack('>H', data[query_start:query_start + 2])[0]
	return domain_name, query_type
	
def parse_ip_header(packet):
	ip_header = packet[:20]
	iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
	src_ip = socket.inet_ntoa(iph[8])
	dest_ip = socket.inet_ntoa(iph[9])
	return src_ip, dest_ip
	
def capture_dns_packets():
	sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
	sock.bind(('0.0.0.0',0))
	with open("dns_queries.log", "a") as log_file:
		print("Capturing DNS Packets...., Press Ctrl+C to stop.")
	
		while True:
			packet = sock.recvfrom(65565)[0]
			src_ip, dest_ip = parse_ip_header(packet)
			udp_header = packet[20:28]
			src_port, dest_port, length, checksum = struct.unpack('!HHHH', udp_header)
		
			if dest_port == 53 or src_port == 53:
				dns_data = packet[28:]
				domain_name, query_type = parse_dns_query(dns_data)
				log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} | Source IP: {src_ip} | Destination IP: {dest_ip} | Domain: {domain_name} | Type: {query_type}\n"
				print(log_entry.strip())
				log_file.write(log_entry)
				log_file.flush()
			
if __name__ == "__main__":
    try:
        capture_dns_packets()
    except KeyboardInterrupt:
        print("\nPacket Sniffer Stopped.")