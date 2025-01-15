#!/usr/bin/env python3
import paramiko
import socket
import time


def ssh_test_all(machine, all_users, all_passwords):
    print("Testing SSH Service")
    client = paramiko.SSHClient()
    grab_banner(machine)
    get_all_possible_key_exchange_algorithms(machine, client)
    test_credentials(machine, client, all_users, all_passwords)


def grab_banner(machine):
    # grab ssh banner
    banner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    banner_socket.connect((machine.ip, 22))
    bytes = banner_socket.recv(1024)
    banner_socket.settimeout(5)
    print(f"Banner: {bytes.decode('utf-8')}")
    # TODO parse banner for it's content - might not be possible as banner will sometimes be custom


def get_all_possible_key_exchange_algorithms(machine, client):
    transport = paramiko.Transport((machine.ip, 22))
    transport.start_client()
    kex_algorithms = transport.get_security_options().kex
    transport.close()
    print(f"Key Exchange Algorithms: {kex_algorithms}")


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
            except:
                continue
            client.close()
    print("Brute Forcing done")
