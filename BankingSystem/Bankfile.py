from Userfile import User
import csv
import pandas
import random
import time 

loading = "\nLOADING..."

def loading_screen(loading):
    for x in range(1, random.randint(2, 5)):
        print(loading)
        time.sleep(1)

class Bank(User):
    def __init__(self, FirstName: str, LastName: str, Email: str, Gender: str, Age: int, BankName : str, Balance: float, Passcode: int):
        super().__init__(
            FirstName, LastName, Email, Gender, Age
        )

        self.BankName = BankName
        self.Balance = Balance
    
    @classmethod
    def identify_bank(cls, queried_name):
        with open('table.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            found = False
            x = 0
            full_name = (item["FirstName"]).lower() + " " + (item["LastName"]).lower()
            if queried_name.lower() == full_name:
                chances = 3
                while not found:
                    passcode = int(input("\nPlease enter the Passcode associated with the desired account in order to access its Bank Details.\nENTER HERE: "))
                    passcode_from_database = int(item["Passcode"])
                    if passcode == passcode_from_database:
                        loading_screen(loading)
                        print("\nSuccessfully accessed the Bank Account!")
                        print(f"\nOwner ({queried_name.title()}) Details\nBank: {item['BankName']}\nBalance: ${item['Balance']}")
                        found = True
                        x = 1
                        break
                    else:
                        print(f"\nThe Passcode ('{passcode}') is incorrect.\nPlease try again.")
                        print(f"\nYou have {chances} chances left.")
                        chances -= 1
                    if chances < 0:
                        print("\nYou have exhausted your number of tries, and are now temporarily blocked from accessing the account.")
                        break
            else:
                print(f"\nUnsucessful. The User ('{queried_name.title()}') does not have an active bank account with us.")

            break
                
    @classmethod
    def create_deposit(cls, queried_name, deposit):
        file = pandas.read_csv('table.csv')
        x = 0
        with open('table.csv', 'r') as f:
            reader_obj = csv.DictReader(f)

            for row in reader_obj:
                found = False
                firstname = (row["FirstName"]).lower()
                x += 1
                if queried_name.lower() == firstname:
                    balance = float(row["Balance"])
                    balance = balance + deposit
                    file.loc[x-1, "Balance"] = balance
                    file.to_csv('table.csv', index = False)
                    found = True
                    print(f"\nThe deposit of ${deposit} was sucessfully created!")
                    break
            if not found:
                print(f"\nThe user ({queried_name}) is not present within our Bank. Please try again.")

    @classmethod
    def take_money(cls, queried_name, amount):
        file = pandas.read_csv('table.csv')
        x = 0
        with open('table.csv', 'r') as f:
            reader_obj = csv.DictReader(f)

            for row in reader_obj:
                found = False
                firstname = (row["FirstName"]).lower()
                x += 1
                if queried_name.lower() == firstname:
                    balance = float(row["Balance"])
                    balance = balance - amount
                    file.loc[x-1, "Balance"] = balance
                    file.to_csv('table.csv', index = False)
                    found = True
                    print(f"\nYou have taken ${amount} from your account.")
                    break
            if not found:
                print(f"\nThe user ({queried_name}) is not present within our Bank. Please try again.")

                    