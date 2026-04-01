# ATM Simulation Program

balance = 10000
correct_pin = 1234

print("===== WELCOME TO ATM =====")

pin = int(input("Enter your PIN: "))

if pin == correct_pin:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your current balance is: ₹", balance)

        elif choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            if deposit > 0:
                balance += deposit
                print("Amount deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw <= balance and withdraw > 0:
                balance -= withdraw
                print("Please collect your cash.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")
    4
    