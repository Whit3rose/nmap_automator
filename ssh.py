#!/usr/bin/env python3
from paramiko import SSHClient

def brute_force_ssh_connection():

client = SSHClient()
def ssh_test_all(machine, all_users, all_passwords):
    print('Testing SSH Service')
    client = SSHClient()
    test_credentials(machine, client, all_users, all_passwords)


def test_credentials(machine, client, all_users, all_passwords):
    print("Testing default passwords and usernames for SSH")
    for user in all_users:
        for password in all_passwords:
            try:
                client.connect(machine.ip, username=user, password=password)
                client.close()
                print(f"FINDING: SSH credentials: {user}:{password}")
            except:
                continue
