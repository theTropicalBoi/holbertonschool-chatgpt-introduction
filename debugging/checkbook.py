class Checkbook:
    def __init__(self):
        # Initialize the checkbook with a balance of 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Add the deposited amount to the balance
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Withdraw the specified amount if sufficient funds are available
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Display the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a new Checkbook instance
    cb = Checkbook()
    while True:
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            # Exit the program if the user types 'exit'
            break
        elif action.lower() == 'deposit':
            try:
                # Prompt the user to enter the deposit amount
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                # Prompt the user to enter the withdrawal amount
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            # Show the current balance
            cb.get_balance()
        else:
            # Handle invalid action commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()
