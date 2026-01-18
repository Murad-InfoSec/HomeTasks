import os
import random


class NumberHunter:
    def __init__(self):
        self.guess=0
        self_secret=0
    
    def start_game(self):
        self.secret=random.randint(1,100)
        while not self.guess == self.secret:

            self._console_render()            
            self._comparison()

    def _console_render(self):
        os.system("cls")
        try:        
           self.guess=int(input("Enter the secret number in range 1-100 u have guessed: "))           
        except ValueError:
            print ("Please enter the number (not a char) :")

    def _comparison(self):
        if self.guess == self.secret:
            print("Congratulations u've found the number!!!")
        elif self.guess > self.secret:
            print("The secret number is greater than ur num.")
        else:
            print("The secret number is smaller than ur num.")
        input()
