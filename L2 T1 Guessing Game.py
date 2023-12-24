#Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number.
#The program should provide hints such as "too high" or "too low" until the correct number is guessed.

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the user's guess to an invalid value
    user_guess = 0

    # Start the game loop
    while user_guess != secret_number:
        try:
            # Get the user's guess
            user_guess = int(input("Guess the number (between 1 and 100): "))

            # Check if the guess is too high, too low, or correct
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number.")
        except ValueError:
            # Handle the case where the user enters a non-integer
            print("Please enter a valid number.")

# Run the game
guess_the_number()
