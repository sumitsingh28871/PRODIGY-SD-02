import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while guess != number_to_guess:
        try:
            # Prompt the user for a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback on the guess
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guessing_game()
