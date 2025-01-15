#!/usr/bin/env python3
from Exscript.protocols import Telnet, exception
from Exscript.account import Account
import socket


def telnet_test_all(machine, all_users, all_passwords):
    print("Testing Telnet Service")
    conn = Telnet()
    test_credentials(machine, conn, all_users, all_passwords)


def test_credentials(machine, conn, all_users, all_passwords):
    print("Testing default passwords and usernames for Telnet")
    for user in all_users:
        for password in all_passwords:
            account = Account(name = user, password = password)
            conn.connect(machine.ip)
            try:
                conn.login(account)
                print(f"FOUND TELNET LOGIN: {user}:{password}")
            except exception.LoginFailure:
                continue
            conn.close()
