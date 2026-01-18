import os
import random


class NumberHunter:
    """Number guessing game class."""
    
    def __init__(self):
        """Initialize game state."""
        self.guess = 0      # Current player guess
        self.secret = 0     # Secret number to guess
    
    def start_game(self):
        """Generate secret number and start game loop."""
        self.secret = random.randint(1, 100)
        while not self.guess == self.secret:
            self._console_render()   # Get user input
            self._comparison()       # Compare and give feedback

    def _console_render(self):
        """Clear console and get user guess input."""
        os.system("cls")
        try:
            self.guess = int(input("Enter the secret number in range 1-100 u have guessed: "))
        except ValueError:
            print("Please enter the number (not a char) :")

    def _comparison(self):
        """Compare guess with secret number and provide feedback."""
        if self.guess == self.secret:
            print("Congratulations u've found the number!!!")
        elif self.guess > self.secret:
            print("The secret number is greater than ur num.")
        else:
            print("The secret number is smaller than ur num.")
        input()
    
