import sys
import json
import os

DATA_FILE = "accounts.json"

def load_accounts():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=2)

def create_account(account_id):
    accounts = load_accounts()
    if account_id in accounts:
        print(f"Error: Account {account_id} already exists.")
        return
    accounts[account_id] = 0
    save_accounts(accounts)
    print(f"Account {account_id} created.")

def deposit(account_id, amount):
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return
    accounts = load_accounts()
    if account_id not in accounts:
        print(f"Error: Account {account_id} does not exist.")
        return
    accounts[account_id] += amount
    save_accounts(accounts)
    print(f"Deposited {amount} to account {account_id}.")

def withdraw(account_id, amount):
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return
    accounts = load_accounts()
    if account_id not in accounts:
        print(f"Error: Account {account_id} does not exist.")
        return
    if accounts[account_id] < amount:
        print("Error: Insufficient balance.")
        return
    accounts[account_id] -= amount
    save_accounts(accounts)
    print(f"Withdrew {amount} from account {account_id}.")

def balance(account_id):
    accounts = load_accounts()
    if account_id not in accounts:
        print(f"Error: Account {account_id} does not exist.")
        return
    print(f"Balance for account {account_id}: {accounts[account_id]}")

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
