import redis

def redis_test_all(machine, all_users, all_passwords):
    print("Testing Redis Service")
    test_credentials(machine, all_users, all_passwords)

# test without password, test default user with password, test username and password
def test_credentials(machine, all_users, all_passwords):
    # test login without credentials
    print("testing login without credentials")
    try:
        redis_connection = redis.Redis(host=machine.ip, port=6379, db=0)
        redis_connection.ping()
        print("Login without credentials successful")
    except redis.exceptions.AuthenticationError:
        pass

    # test login for default user
    print("testing login for default account")
    for password in all_passwords:
        try:
            redis_connection = redis.Redis(host=machine.ip, port=6379, username="default", password=password, db=0)
            redis_connection.ping()
            print(f"Login successful for default user and password {password}")
        except redis.exceptions.AuthenticationError:
            pass

    # test login with rainbow table
    print("testing login with provided usernames and passwords")
    for user in all_users:
        for password in all_passwords:
            try:
                redis_connection = redis.Redis(host=machine.ip, port=6379, username=user, password=password, db=0)
                redis_connection.ping()
                print(f"Login successful for {user}:{password}")
            except redis.exceptions.AuthenticationError:
                pass
