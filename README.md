# Online Transaction Management System

A comprehensive banking system built with Python and MySQL that allows users to manage their accounts, perform transactions, and track their banking activities.

## 🌟 Features

- **User Authentication**
  - Sign up new users
  - Login with email and password
  - Secure logout

- **Account Management**
  - Create new bank accounts (Savings/Current)
  - View account details
  - Secure PIN-based authentication for transactions

- **Transaction Operations**
  - Deposit money
  - Withdraw money (with PIN verification)
  - View transaction history

- **Personal Information Management**
  - Update personal details (name, phone, email)
  - Change account password
  - Manage user profile

## 📋 System Requirements

- Python 3.x
- MySQL Database
- Python Packages:
  - mysql-connector-python
  - prettytable

## 🚀 Setup Instructions

1. **Install Required Packages**
   ```bash
   pip install mysql-connector-python prettytable
   ```

2. **Database Configuration**
   - Make sure MySQL server is running on localhost
   - The default credentials in the code are:
     - Username: root
     - Password: 123456
   - You can modify these in the `MYSQLconnectionCheck()` and `MYSQLconnection()` functions if needed

3. **Run the Application**
   ```bash
   python Online_Transaction_Management_system.py
   ```

## 💻 Usage Guide

### Main Menu
The system provides the following main options:
1. Sign Up - Create a new user account
2. Login - Access your account
3. Personal Details - Enter your personal information
4. Menu Screen - Access the main banking functions

### Banking Menu
After logging in, you can:
1. View Details - Check personal, account, and transaction information
2. Create New Account - Open a new bank account
3. Deposit - Add funds to your account
4. Withdraw - Remove funds from your account
5. Update - Modify your personal information
6. Logout - Securely exit the system

## 🔒 Security Features

- Password protection for user accounts
- PIN verification for withdrawals
- Limited PIN entry attempts with account blocking after 3 failed attempts

## 📊 Database Schema

The system uses several MySQL tables:
- `LOGIN` - Stores user authentication details
- `DETAILS` - Stores personal information
- `ACCOUNT` - Stores account information
- `DEPOSIT` - Records deposit transactions
- `WITHDRAW` - Records withdrawal transactions

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## 📝 License

This project is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## 📞 Contact

Created by [@Sargamchicholikar](https://github.com/Sargamchicholikar) - feel free to contact me!
