import sys

accounts = {}

def create_account(account_id):
    accounts[account_id] = 0
    print(f"Account {account_id} created.")

def deposit(account_id, amount):
    if account_id in accounts:
        accounts[account_id] += amount
        print(f"Deposited {amount} to account {account_id}.")
    else:
        print(f"Account {account_id} does not exist.")

def withdraw(account_id, amount):
    if account_id in accounts:
        if accounts[account_id] >= amount:
            accounts[account_id] -= amount
            print(f"Withdrew {amount} from account {account_id}.")
        else:
            print(f"Withdrawal failed: Insufficient funds in account {account_id}.")
    else:
        print(f"Account {account_id} does not exist.")

def balance(account_id):
    if account_id in accounts:
        print(f"Balance for account {account_id}: {accounts[account_id]}")
    else:
        print(f"Account {account_id} does not exist.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 bank.py [create_account|deposit|withdraw|balance] args")
        return
    cmd = sys.argv[1]
    if cmd == "create_account":
        create_account(sys.argv[2])
    elif cmd == "deposit":
        deposit(sys.argv[2], int(sys.argv[3]))
    elif cmd == "withdraw":
        withdraw(sys.argv[2], int(sys.argv[3]))
    elif cmd == "balance":
        balance(sys.argv[2])
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()