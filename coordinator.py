#!/usr/bin/env python3

import paramiko
import socket

import nmap_parser
import test_ssh
import test_telnet
import test_redis

nmap_filename = 'test_nmap.xml'
all_machines = nmap_parser.parse_nmap_file(nmap_filename)

password_file = "passwords.txt"
users_file = "users.txt"

print("Setting up configuration")
with open(password_file, 'r') as password_file_handler:
    all_passwords = password_file_handler.read().split("\n")

with open(users_file, 'r') as users_file_handler:
    all_users = users_file_handler.read().split("\n")

# check for common ports, then use the common attacks/enumerations
print("Starting Tests")
print("-------------------------------")
for machine in all_machines:
    print(f"Starting Tests for {machine.ip}")
    for port in machine.ports:
        print(f"Open Ports: {port.portid}, Running Protokol: {port.protocol}")

        # SSH
        if port.portid == "22":
            test_ssh.ssh_test_all(machine, all_users, all_passwords)
        # TELNET
        if port.portid == "23":
            test_telnet.telnet_test_all(machine, all_users, all_passwords)
        # Redis
        if port.portid == "6379":
            test_redis.redis_test_all(machine, all_users, all_passwords)
