import random
from art import logo

def get_random_number(end):
    """
    Generates a random number between 1 and a specified upper limit.

    Args:
        end (int): The upper limit of the random number range.

    Returns:
        int: A random number between 1 and the specified end value.
    """
    return random.randint(1, end)

def get_game_difficult(difficulty):
    """
    Determines the number of attempts based on the selected difficulty level.

    Args:
        difficulty (str): The difficulty level chosen by the user, either 'easy' or 'hard'.

    Returns:
        int: Number of attempts; 10 for 'easy' and 5 for 'hard'.
    """
    return 10 if difficulty == 'easy' else 5

def check_guess(guess_number, target_number):
    """
    Compares the guessed number with the target number and provides feedback.

    Args:
        guess_number (int): The number guessed by the user.
        target_number (int): The actual target number that the user is trying to guess.

    Returns:
        str: A message indicating whether the guess was correct, too high, or too low.
    """
    if guess_number == target_number:
        return f'You got it! The answer was {guess_number}'
    elif guess_number > target_number:
        return 'Too High.'
    else:
        return 'Too Low.'

def main():
    """
    Implements the main logic of the number guessing game:
    
    - The user must guess a random number between 1 and 100.
    - The user selects a difficulty level, which determines the number of allowed attempts.
    - After each guess, feedback is provided whether the guess is too high, too low, or correct.
    - If the user runs out of guesses without guessing correctly, the game ends with a loss.
    """
    end_number = 100
    target_number = get_random_number(end_number)  # Generate a random number

    print(logo)  # Display the game logo
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {end_number}.")

    # Ask the user to choose a difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guess_attempt = get_game_difficult(difficulty)  # Set the number of attempts based on difficulty

    # Main game loop: Continue until user runs out of guesses or guesses correctly
    while guess_attempt > 0:
        print(f'You have {guess_attempt} attempts remaining to guess the number.')

        guess = int(input('Make a guess: '))  # Get the user's guess
        check = check_guess(guess, target_number)  # Check if the guess is correct
        
        if guess == target_number:
            print(check)  # Print success message if correct
            break  # Exit the loop if the guess is correct
        
        print(check)  # Print feedback if the guess is too high or too low
        guess_attempt -= 1  # Decrease the remaining number of attempts
        
        if guess_attempt == 0:
            print("You've run out of guesses, you lose.")  # Inform the user if they run out of guesses
        else:
            print("Guess Again.")  # Ask the user to guess again if they have attempts left

# Start the number guessing game
main()
