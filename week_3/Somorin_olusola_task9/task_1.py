# You are to design a mock USSD interface for a mobile service.
# Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences (\n) for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.
balance = 0
dataplan = {
    "Daily plan": {"1.5GB": 300, "4GB": 800},
    "Weekly plan": {"15GB": 3000},
    "Monthly plan": {"50GB": 7000}
}
print("\t== Welcome to MTN, your number one service provider ==")

while True:
    print("\nService options:")
    print("1. Check Airtime Balance")
    print("2. Recharge Airtime")
    print("3. Buy Data")
    print("4. Exit")
        
    choice = input("Enter choice: ")
    if choice == "1":
        print (f"Your airtime balance is: {balance}")
    elif choice == "2":
        amount = float(int(input("Enter the amount of Airtime you want to purchase: ")))
        balance += amount
        print(f"You have successfully purchased ₦{amount} Airtime.\n Your new airtime balance is {balance}.")
    elif choice == "3":
        print("\nBuy Data Plans")
        print("1. Daily\n2. Weekly\n3. Monthly")
        datachoice = input("Enter choice: ")
        if datachoice == "1":
            print("\nDaily plan")
            print("1. ₦300 = 1.5GB\n2. ₦800 = 4GB")
            dailychoice = input("Enter choice: ")
            if dailychoice == "1":
                if dataplan["Daily plan"]["1.5GB"] <= balance:
                    balance -= dataplan["Daily plan"]["1.5GB"]
                    print(f"You have successfully purchased 1.5GB daily plan.\nYour new airtime balance is: {balance}  ")
                else:
                    print("Insufficient funds.")
            elif dailychoice == "2":
                if dataplan["Daily plan"]["4GB"] <= balance:
                    balance -= dataplan["Daily plan"]["4GB"]
                    print(f"You have successfully purchased 4GB daily plan.\nYour new airtime balance is {balance}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid option. Try again.")
        elif datachoice == "2":
            print("\nWeekly plan")
            print("1. ₦3000 = 15GB")
            weeklychoice = input("Enter choice: ")
            if weeklychoice == "1":
                if dataplan["Weekly plan"]["15GB"] <= balance:
                    balance -= dataplan["Weekly plan"]["15GB"]
                    print(f"You have successfully purchased 15GB weekly plan.\nYour new airtime balance is {balance}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid option. Try again.")
        elif datachoice == "3":
            print("\nMonthly plan")
            print("1. ₦7000 = 50GB")
            monthlyplan = input("Enter choice: ")
            if monthlyplan == "1":
                if dataplan["Monthly plan"]["50GB"] <= balance:
                    balance -= dataplan["Monthly plan"]["50GB"]
                    print(f"You have successfully purchased 50GB monthly plan.\nYour new airtime balance is {balance}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid option. Try again.")
        else:
            print("Invalid option. Try again.")
    elif choice == "4":
        print("Thank you for using MTN. Keep browsing")
        break
    else:
        print("Invalid option. Try again.")
