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
        print("Your balance is ", balance)

    elif action == 2:
        deposit = int(input("Enter amount to deposit: "))
        balance = balance + deposit
        print("Deposit successful. New balance = ", balance)

    elif action == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if balance > withdraw:
            balance = balance - withdraw
            print("Withdrawal successful. New balance = ", balance)
        else:
            print("Insufficient funds!")

    elif action == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid numbner.")