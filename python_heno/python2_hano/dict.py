'''Project 1 (Explain in Class): 🏦 ATM Banking System (Best Choice)
Features
Login using Account Number
PIN Verification
Deposit
Withdraw
Balance Check
Transaction History
Change PIN
Show Unique Transaction Types
Exit'''

# ================================
#        ATM BANKING SYSTEM
# ================================

print("=" * 40)
print("      WELCOME TO PYTHON ATM")
print("=" * 40)

# Dictionary (Accounts)
accounts = {
    "1001": {
        "name": "Swaraj",
        "pin": "1234",
        "balance": 5000,
        "history": []
    },
    "1002": {
        "name": "Rahul",
        "pin": "5678",
        "balance": 8000,
        "history": []
    },
    "1003": {
        "name": "Priya",
        "pin": "4321",
        "balance": 12000,
        "history": []
    }
}

# Tuple (Menu)
menu = (
    "1. Balance Check",
    "2. Deposit",
    "3. Withdraw",
    "4. Transaction History",
    "5. Change PIN",
    "6. Show Unique Transaction Types",
    "7. Show All Accounts",
    "8. Exit"
)

# Login
account_no = input("Enter Account Number : ").strip()

if account_no in accounts:

    pin = input("Enter PIN : ").strip()

    if pin == accounts[account_no]["pin"]:

        print("\nLogin Successful")
        print("Welcome", accounts[account_no]["name"].title())

        while True:

            print("\n========= MENU =========")

            for item in menu:
                print(item)

            choice = input("Enter Choice : ")

            # Balance
            if choice == "1":

                print("Available Balance : ₹", accounts[account_no]["balance"])

            # Deposit
            elif choice == "2":

                amount = int(input("Enter Deposit Amount : "))

                if amount > 0:

                    accounts[account_no]["balance"] += amount

                    accounts[account_no]["history"].append("Deposit ₹" + str(amount))

                    print("Amount Deposited Successfully")

                else:
                    print("Invalid Amount")

            # Withdraw
            elif choice == "3":

                amount = int(input("Enter Withdraw Amount : "))

                if amount <= accounts[account_no]["balance"]:

                    accounts[account_no]["balance"] -= amount

                    accounts[account_no]["history"].append("Withdraw ₹" + str(amount))

                    print("Please Collect Your Cash")

                else:

                    print("Insufficient Balance")

            # Transaction History
            elif choice == "4":

                history = accounts[account_no]["history"]

                if len(history) == 0:

                    print("No Transactions")

                else:

                    print("\nTransaction History")

                    for transaction in history:
                        print(transaction)

            # Change PIN
            elif choice == "5":

                old_pin = input("Enter Old PIN : ")

                if old_pin == accounts[account_no]["pin"]:

                    new_pin = input("Enter New PIN : ")

                    accounts[account_no]["pin"] = new_pin

                    accounts[account_no]["history"].append("PIN Changed")

                    print("PIN Updated Successfully")

                else:

                    print("Wrong PIN")

            # Unique Transaction Types
            elif choice == "6":

                transaction_types = set()

                for transaction in accounts[account_no]["history"]:

                    word = transaction.split()[0]

                    transaction_types.add(word)

                print("\nUnique Transaction Types")

                if len(transaction_types) == 0:
                    print("No Transactions")
                else:
                    for item in transaction_types:
                        print(item)

            # Dictionary Methods
            elif choice == "7":

                print("\nAvailable Accounts")

                print("Keys :", accounts.keys())

                print("\nValues")

                for value in accounts.values():
                    print(value["name"])

                print("\nItems")

                for key, value in accounts.items():
                    print(key, "->", value["name"])

            # Exit
            elif choice == "8":

                print("\nThank You For Using Python ATM")
                break

            else:

                print("Invalid Choice")

    else:

        print("Incorrect PIN")

else:

    print("Account Not Found")
    