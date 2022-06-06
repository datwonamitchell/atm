def show_balance(balance):
    print(f'Current Balance: {balance}')


def deposit(balance):
    while True:
        amount = input("Enter amount to deposit: ")
        if(amount == '' or amount == 0):
            print(f'Error: Deposit amount is too low!')
            continue
        float_amount = float(amount)
        if(deposit_validation(balance, float_amount) is False):
            return balance
        return balance + float_amount


def deposit_validation(balance, deposit_amount):
    if (deposit_amount < 0 or deposit_amount == ''):
        print(f'Error: Deposit amount is too low!')
        return False
    else:
        return True


def withdraw_validation(balance, withdraw_amount):
    if (balance < withdraw_amount):
        print(f'Error: Withdrawal amount is too high!')
        return False
    elif (withdraw_amount < 0 or withdraw_amount == ''):
        print(f'Error: Withdrawal amount is too low!')
        return False
    else:
        return True


def withdraw(balance):
    while True:
        amount = input("Enter amount to withdraw: ")
        if(amount == '' or amount == 0):
            print(f'Error: Withdrawal amount is too low!')
            continue
        float_amount = float(amount)
        if (withdraw_validation(balance, float_amount) is False):
            return balance
        else:
            return balance - float_amount


def logout(name):
    print(f'Goodbye {name}!')
