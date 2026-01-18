import os
import random


def recursive_comparison(guess, attempts, secret):
    """Recursively compare guess with secret number until correct."""
    attempts += 1
    
    if guess == secret:
        print("Congratulations!!")
        input()
        return attempts
    
    elif guess < secret and attempts != 1:
        print("The secret number is greater than guess!")
    elif guess > secret:
        print("The secret number is smaller than guess!")
    
    input()
    os.system("cls")
    new_guess = int(input("Enter ur guess in range 1-100 "))
    
    return recursive_comparison(new_guess, attempts, secret)


def main():
    """Main game function - generates secret number and starts game."""
    secret = random.randint(1, 100)
    guess = 0
    attempts = 0
    
    guess = int(input("Enter ur guess in range 1-100: "))
    recursive_comparison(guess, attempts, secret)


