""" This program system creates a customer account, displays the customer's account information, and allows deposits and withdrawals.
    The program also checks if there is enough money in the account for a withdrawal"""


# Create an Account class
class Account:

    # Initialise the account number and starting balance
    def  __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

     # Add money to the account balance
    def deposit(self, amount):
        self.balance += amount
        # Display the amount deposited and the new balance
        print(f"${amount} deposited. New balance: ${self.balance}")

    # Withdraw money from the account
    def withdraw(self, amount):

         # Check if the withdrawal amount is more than the balance
        if amount>self.balance:
            # If there is not enough money, print an error message
            print("Insufficient funds!")

        # If there is enough money, subtract the amount from the balance
        else:
            self.balance -= amount
            # Display the amount withdrawn and the new balance
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    # Display the account number and current balance
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")




# Create a Customer class
class Customer:

    # Initialise the customer's name and account
    def __init__(self, name, account):
        self.name = name
        self.account = account

    # Display the customer's information
    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        # Display the customer's account balance
        self.account.display_balance()


# Create a Transaction class
class Transaction:

    # Initialise the account, amount and transaction type
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        # Process the transaction
        self.process_transaction()

     # type of transaction being made
    def process_transaction(self):

        # If the transaction is a deposit, add money to the account
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)

        # If the transaction is a withdrawal, remove money from the account
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)

        # If the transaction type is invalid, print an error message
        else:
            print("Invalid transaction type!")


#Test the functionality of the banking system

#creating an account for a customer
account1=Account (account_number=67890, balance=500)
# Create a customer and connect them to account1
customer1=Customer(name="Ruaa", account=account1)

#Displaying customer information
customer1.display_customer_info()

#Performing transactions
Transaction1=Transaction(account=account1, amount=200, transaction_type="deposit")
Transaction2=Transaction(account=account1, amount=400, transaction_type="withdraw")

# Displaying customer information after transactions
customer1.display_customer_info()

#Assertion 1: if the balance is equal to 300 after the transactions, the test passes
