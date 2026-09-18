balance = 20000
correct_pin = "1234"

def check_balance():
    global balance
    print(f"Your Account have {balance} Rs.")

def deposit():
    global balance
    amount = float(input("Enter your Amount: "))
    if amount > 0:
        balance += amount
        print(f"Your {amount} Rs Successfully Deposit")
    else:
        print("Invalid Amount")

def withdraw():
    global balance
    amount = float(input("Enter your Amount: "))

    if amount < 0:
        print("Invalid Amount")
    elif amount > balance:
        print("Insufficient Amount")
    else:
        balance -= amount
        print(f"{amount} Successfully Withdraw")

pin = input("Enter your pin: ")

if pin == correct_pin:
    while True:
        print("\n------ATM------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choise = input("Enter your Choise: ")

        if choise == "1":
            check_balance()
        elif choise == "2":
            deposit()
        elif choise == "3":
            withdraw()
        elif choise == "4":
            break
        else:
            print("Invalid Choise Please Chosse Correct One Thankyou")

else:
    print("InValid Pin")