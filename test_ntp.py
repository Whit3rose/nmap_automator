#!/usr/bin/env python3
import socket

def ntp_test_all(machine):
    print("Testing NTP Service")
    ntp_test_monlist(machine)

def ntp_test_monlist(machine):
    print("checking if ntp monlist is enabled")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ntppacket = bytearray(48)
    ntppacket[0] = 0x17
    ntppacket[1] = 0x00
    ntppacket[2] = 0x03
    ntppacket[3] = 0x2a

    server = socket.gethostbyname(machine.ip)
    sock.sendto(ntppacket, (server, 123))
    sock.settimeout(5)
    try:
        data, address = sock.recvfrom(1024)
    except socket.timeout:
        pass

    if data:
        print("NTP monlist active")
