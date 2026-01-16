import sys,os

## Task 1 - ATM
class BankingATM:
    """
    BankingATM class represents an Automated Teller Machine (ATM).
    It provides basic banking operations like checking balance, depositing, and withdrawing money.
    """
    def __init__(self):
        """Initialize the ATM with a default balance of 500 and main menu options."""
        self.balance=500  # Initial account balance
        self.main_menu={  # Dictionary storing menu options
                1:"1 - Balansı yoxla.",  # Check balance
                2:"2 - Mədaxil et",      # Deposit money
                3:"3 - Nağdlaşdır",      # Withdraw money
                4:"4 - Çıxış"           # Exit
        }
    
    def show_balance(self):
        """Display the current account balance."""
        print(f"Cari balansınız: {self.balance}")
    
    def deposit(self):
        """Add money to the account balance."""
        value=int(input("Artirmaq istediyiniz meblegi elave edin:\n"))
        self.balance+=value  # Increase balance by deposited amount
        print("Təbrikler, balansınız artırıldı.")
        self.show_balance()

    def withdrawal(self):
        """Remove money from the account balance."""
        value=int(input("Cixartmaq istediyiniz meblegi elave edin:\n"))
        self.balance-=value  # Decrease balance by withdrawn amount
        print(f"Hesabinizdan {value} cixarildi.")
        self.show_balance()

    def __str__(self):
        """Return a formatted string representation of the main menu."""
        return f"{self.main_menu[1]}\n{self.main_menu[2]}\n{self.main_menu[3]}\n{self.main_menu[4]}"  

        
# Create an instance of BankingATM
ATM=BankingATM()
# Get all methods and attributes of the ATM instance
methods = ATM.__dir__()
# Filter to only include public methods (excluding private methods starting with '_')
public_methods = [m for m in methods if not m.startswith('_')]


# Main program loop - runs until user chooses to exit (option 4)
while True:
    os.system("cls")  # Clear the console screen
    print(ATM)  # Display the menu
    button=int(input())  # Get user's menu selection
   
    # Exit the program if user selects option 4
    if button == 4:
        break

    os.system("cls")  # Clear the console screen again

    # Dynamically get and call the selected method
    # public_methods[button+1] because button 1 maps to index 2 (after __init__ and __str__)
    method=getattr(ATM,public_methods[button+1])
    method()  # Execute the selected method
    input("\nPress any key to continue!")  # Pause before showing menu again
