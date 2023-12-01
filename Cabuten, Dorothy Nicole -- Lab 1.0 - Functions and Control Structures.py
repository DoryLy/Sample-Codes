balance = 100.00

class ATM:
    def check_balance(self):
        global balance
        print("\n-------------------------------------------------------------")
        print(f"          :: Your current balance is: {balance} PHP ::")
        print("-------------------------------------------------------------")

    def withdraw(self, amount):
        global balance
        if amount > balance:
            print("\n-------------------------------------------------------------")
            print("          :: Insufficient funds. Withdrawal denied. ::")
            print("-------------------------------------------------------------")
        else:
            balance -= amount
            print("\n-------------------------------------------------------------")
            print(f"         :: Withdrawal of {amount} PHP successful. ::")
            print("-------------------------------------------------------------")
            self.check_balance()

    def deposit(self, amount):
        global balance
        if amount > 0:
            balance += amount
            print("\n-------------------------------------------------------------")
            print(f"           :: Deposit of {amount} PHP successful. ::")
            print("-------------------------------------------------------------")
            self.check_balance()
        else:
            print("\n-------------------------------------------------------------")
            print("          :: Please enter a valid deposit amount. ::")
            print("-------------------------------------------------------------")

    def start(self):
        print("*************************************************************")
        print()
        print("              WELCOME TO THE UC ATM MACHINE")
        print()
        print("*************************************************************")
        while True:
            print("\nCommands: \n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Exit Application")
            choice = input("\nPlease enter the number of the command you want to perform: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                print("\n-------------------------------------------------------------")
                amount = float(input("             Enter the amount to withdraw: "))
                print("-------------------------------------------------------------")
                self.withdraw(amount)
            elif choice == '3':
                print("\n-------------------------------------------------------------")
                amount = float(input("              Enter the amount to deposit: "))
                print("-------------------------------------------------------------")
                self.deposit(amount)
            elif choice == '4':
                print("\n*************************************************************")
                print()
                print("         Thank you for using the DNC ATM. Goodbye!")
                print()
                print("*************************************************************")
                break
            else:
                print("\n-------------------------------------------------------------")
                print("    Invalid choice. Please enter a valid command number.")
                print("-------------------------------------------------------------")

if __name__ == "__main__":
    atm = ATM()
    atm.start()