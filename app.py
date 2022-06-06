from banking_pkg.account import show_balance, withdraw, logout, deposit

name = ""
pin = ""
balance = 0.00


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


def name_validation(name):
    while True:
        if(len(name) > 10):
            print("Error: The maximum name length is 10 characters.")
            return False
        elif (len(name) < 1):
            print("Error: The minimum name length is 1 character.")
            return False
        else:
            return True


def pin_validation(pin):
    while True:
        if(len(pin) != 4):
            print("Error: PIN length must be 4 numbers.")
            return False
        else:
            return True


def atm_options(user):
    while True:
        global balance
        atm_menu(user)
        option = input("Choose an option: ")
        if(option == "1"):
            show_balance(balance)
        elif (option == "2"):
            balance = deposit(balance)
            show_balance(balance)
        elif (option == "3"):
            balance = withdraw(balance)
            show_balance(balance)
        elif (option == "4"):
            logout(user)
            break
        else:
            print("Error: Invalid Option, Please enter 1, 2, 3, or 4")
            continue

# Task 3


def login_prompt(name_to_validate, pin_to_validate):
    while True:
        print("LOGIN")
        login_name = input("Enter name: ")
        pin_name = input("Enter PIN: ")
        # Validate Login
        if(login_name == name_to_validate and pin_name == pin_to_validate):
            print("Login successful!")
            atm_options(login_name)
            break
        else:
            print("Error: Invalid credentials!")
            continue

# Bonus Task 1 & 2 (Contains Task 2)


def name_input():
    while True:
        global name
        name = input("Enter name to register: ")
        validate_name = name_validation(name)
        if (validate_name is False):
            continue
        else:
            break


def pin_input():
    while True:
        global pin
        pin = input("Enter PIN: ")
        validate_pin = pin_validation(pin)
        if (validate_pin is False):
            continue
        else:
            break


def registration_prompt():
    while True:
        print("          === Automated Teller Machine ===          ")
        name_input()
        pin_input()
        print(f'{name} has been registered with a starting balance of ${balance}')
        login_prompt(name, pin)
        break


registration_prompt()
