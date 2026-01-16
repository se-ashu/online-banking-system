# 🏦 Online Banking System (Python)

A simple **Online Banking System** built with Python that demonstrates **Object-Oriented Programming (OOP)**, **File Handling**, and **Exception Handling**.  
This project simulates basic banking operations such as deposits, withdrawals, transfers, and balance inquiries, while persisting account data in a text file.

---

## ✨ Features
- **Account Management**
  - Base `Account` class with deposit, withdraw, and balance methods.
  - Specialized `SavingsAccount` and `CheckingAccount` classes.
- **File Handling**
  - Accounts are saved to and loaded from `accounts.txt`.
  - Automatically creates default accounts if no file exists.
- **Exception Handling**
  - Handles invalid inputs (negative amounts, overdraft limits, insufficient balance).
  - Graceful error messages for user mistakes.
- **Banking Operations**
  - Deposit into Savings Account
  - Withdraw from Checking Account
  - Transfer funds between accounts
  - Display balances

---

## 📂 Project Structure
```
├── accounts.txt        # Stores account data (auto-created if missing)
├── banking.py          # Main program file
└── README.md           # Project documentation
```

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/online-banking-system.git
   cd online-banking-system
   ```

2. Run the program:
   ```bash
   python banking.py
   ```

3. Use the interactive menu:
   ```
   --- Online Banking Menu ---
   1. Deposit (Savings)
   2. Withdraw (Checking)
   3. Transfer (Savings → Checking)
   4. Show Balances
   5. Exit
   ```

---

## 🛠️ Example Usage
- Deposit ₹1000 into Savings:
  ```
  Enter choice: 1
  Enter deposit amount: 1000
  Deposit successful
  ```
- Withdraw ₹500 from Checking:
  ```
  Enter choice: 2
  Enter withdrawal amount: 500
  Withdrawal successful
  ```
- Transfer ₹2000 from Savings → Checking:
  ```
  Enter choice: 3
  Enter transfer amount: 2000
  Transfer successful
  ```

---

## 📖 Concepts Demonstrated
- **Object-Oriented Programming (OOP)**  
  Inheritance, encapsulation, and method overriding.
- **File Handling**  
  Persistent storage of account data in `accounts.txt`.
- **Exception Handling**  
  Prevents invalid transactions and provides user-friendly error messages.

---

## 🔮 Future Enhancements
- Add support for multiple accounts.
- Implement interest calculation for savings.
- Add user authentication (PIN/password).
- Use a database (SQLite/MySQL) instead of text files.

```
