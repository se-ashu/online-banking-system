# =========================
# Online Banking System
# With File & Exception Handling
# =========================

FILE_NAME = "accounts.txt"

# -------- Base Account Class --------
class Account:
    def __init__(self, acc_no, balance):
        self.account_number = acc_no
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

    def get_balance(self):
        return self._balance


# -------- Savings Account --------
class SavingsAccount(Account):
    def __init__(self, acc_no, balance, interest):
        super().__init__(acc_no, balance)
        self.interest_rate = interest


# -------- Checking Account --------
class CheckingAccount(Account):
    def __init__(self, acc_no, balance, overdraft):
        super().__init__(acc_no, balance)
        self.overdraft_limit = overdraft

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount


# -------- File Handling --------
def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        for acc in accounts:
            if isinstance(acc, SavingsAccount):
                file.write(f"Savings,{acc.account_number},{acc._balance},{acc.interest_rate}\n")
            else:
                file.write(f"Checking,{acc.account_number},{acc._balance},{acc.overdraft_limit}\n")


def load_accounts():
    accounts = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == "Savings":
                    accounts.append(SavingsAccount(data[1], float(data[2]), float(data[3])))
                else:
                    accounts.append(CheckingAccount(data[1], float(data[2]), float(data[3])))
    except FileNotFoundError:
        pass
    return accounts


# -------- Transfer --------
def transfer(from_acc, to_acc, amount):
    from_acc.withdraw(amount)
    to_acc.deposit(amount)


# =========================
# Main Program
# =========================
accounts = load_accounts()

# Create default accounts if file empty
if not accounts:
    accounts.append(SavingsAccount("SA101", 5000, 5))
    accounts.append(CheckingAccount("CA101", 3000, 2000))

savings = accounts[0]
checking = accounts[1]

while True:
    print("\n--- Online Banking Menu ---")
    print("1. Deposit (Savings)")
    print("2. Withdraw (Checking)")
    print("3. Transfer (Savings → Checking)")
    print("4. Show Balances")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            amt = float(input("Enter deposit amount: "))
            savings.deposit(amt)
            print("Deposit successful")

        elif choice == 2:
            amt = float(input("Enter withdrawal amount: "))
            checking.withdraw(amt)
            print("Withdrawal successful")

        elif choice == 3:
            amt = float(input("Enter transfer amount: "))
            transfer(savings, checking, amt)
            print("Transfer successful")

        elif choice == 4:
            print(f"Savings Balance: ₹{savings.get_balance()}")
            print(f"Checking Balance: ₹{checking.get_balance()}")

        elif choice == 5:
            save_accounts(accounts)
            print("Data saved. Thank you!")
            break

        else:
            print("Invalid menu choice")

    except ValueError as e:
        print("Error:", e)

    except Exception:
        print("Something went wrong")
