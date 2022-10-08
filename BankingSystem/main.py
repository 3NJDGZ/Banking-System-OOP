from Userfile import User
from Bankfile import Bank
import time 
import random

running = True 
loading = "\nLOADING..."

def loading_screen(loading):
    for x in range(1, random.randint(2, 5)):
        print(loading)
        time.sleep(1)

def new_account():
    firstname = input("\nFirst Name: ") 
    lastname = input("\nLast Name: ") 
    email = input("\nEmail: ")
    gender = input("\nGender: ")
    age = int(input("\nAge: "))
    bankname = input("\nBank: ")
    balance = float(input("\nBalance: "))
    valid = False

    while not valid:
        passcode = int(input("\nEnter Passcode (NUMBERS ONLY excluding 0s): "))
        passcode = str(passcode)
        length = len(passcode)
        if length != 6:
            print(f"\nYour Passcode ('{passcode}') should only be 6 digits long.\nPlease try again.")
        else:
            valid = True

    passcode = int(passcode)

    loading_screen(loading)
    User.register_user(firstname, lastname, email, gender, age, bankname, balance, passcode)
    print("\nSuccessfully Registered!")

while running:
    print("\nHello! Welcome to Dean's Bank.")
    answer = input("\n***OPTIONS:***\n1) SEE BANK DETAILS\n2) SEE USER DETAILS\n3) CREATE A NEW ACCOUNT\n4) CREATE A DEPOSIT\n5) TAKE MONEY OUT\n6) QUIT\nENTER HERE (1-6): ")
    if answer == '1':
        print("\nOk before we get your Bank Details, we will need the Full Name associated with that specific bank account.")
        name = input("\nEnter Name: ")
        loading_screen(loading)
        Bank.identify_bank(name)
    elif answer == '2':
        print("\nOk before we get your User Details, we will need the Full Name associated with that specific bank account.")
        name = input("\nEnter Name: ")
        loading_screen(loading)
        User.identify_user(name)
    elif answer == '3':
        new_account()
    elif answer == '4':
        queried_name = input("\nEnter First Name of the desired account: ")
        deposit = float(input("\nHow much money would you like to deposit?\nENTER HERE: "))
        loading_screen(loading)
        Bank.create_deposit(queried_name, deposit)
    elif answer == '5':
        queried_name = input("\nEnter First Name of the desired account: ")
        amount = float(input("\nHow much money would you like to take out?\nENTER HERE: "))
        loading_screen(loading)
        Bank.take_money(queried_name, amount)
    elif answer == '6':
        running = False
    else:
        print("\nInvalid input. Please try again.")
print("See you later!")  
