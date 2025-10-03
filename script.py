balance = int(1000)
action = 0

print("Welcome to the ATM")
print("Your balance is", balance)

while True:

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    action = int(input("Choose an option: "))

    if action == 1:
        print("Option 1")

    elif action == 2:
        print("Option 2")

    elif action == 3:
        print("Option 3")

    else:
        print("Goodbye!")
        break