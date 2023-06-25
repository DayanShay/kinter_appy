import MetaTrader5 as mt5

def connect_to_mt4(account, password, server):
    # Connect to MetaTrader 4
    if not mt5.initialize():
        print("Failed to initialize MetaTrader 5",mt5.last_error())
        return False
    print("success to initialize MetaTrader 5")
    return True

def login_to_account(account, password, server):
    # Log in to the account
    login_result = mt5.login(login=account,server=server,password=password)
    if login_result:
        print("Login successful")
    else:
        print("Login failed:", mt5.last_error())

def disconnect_from_mt4():
    # Disconnect from MetaTrader 4
    mt5.shutdown()


# Account details
account_number = 74191653  # Replace with your account number
account_password = "Aa7946130"  # Replace with your account password
broker_server = "Ava-Real 1"  # Replace with your broker's server name

# Connect to MetaTrader 4
def get_accunt_info():
    info = mt5.account_info()
    print(info)

if connect_to_mt4(account=account_number,password=account_password,server=broker_server):
    # Log in to the account
    login_to_account(account_number, account_password, broker_server)


    get_accunt_info()


    # Disconnect from MetaTrader 4
    disconnect_from_mt4()
