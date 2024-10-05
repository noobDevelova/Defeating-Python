import random

icons = [
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
""" 
____
|/   |
|   
|    
|    
|    
|
|_____
"""
]

def generate_random_words():
    """
    Generates a random word from a predefined list of words.
    
    Returns:
        str: A random word selected from the list ['mouse', 'walking', 'jealous', 'sitting'].
    """
    random_words = ['mouse', 'walking', 'jealous', 'sitting']
    word = random.choice(random_words)  
    return word

def generate_blank_words():
    """
    Generates a blank word (a list of underscores) and the corresponding target word.

    Returns:
        list: A list containing two lists:
            - The first list contains underscores ('_') representing each letter of the target word.
            - The second list contains the individual characters of the target word.
    """
    generated_word = generate_random_words()
    separated_word = list(generated_word)  # Convert the word to a list of individual characters
    blanks = list('_' * len(separated_word))  # Create a list of underscores with the same length as the word
    return [blanks, separated_word]  # Return both the blank version and the target word

def run_hangman():
    """
    The main function to run the Hangman game.
    
    The player is asked to guess letters of a hidden word. For each wrong guess, they lose one life, and 
    the hangman drawing progresses. The game ends when the player either guesses the entire word or runs out 
    of lives.
    
    While loop structure:
        - The game continues while the player has lives remaining.
        - On each iteration, the player guesses a character.
        - If the guessed character is in the target word, it is revealed in the blanks.
        - If the guessed character is not in the word, the player loses a life and the hangman icon is updated.
        - The game ends when the player has no remaining lives or guesses the word correctly.
    """
    remain_life = 6  # The player starts with 6 lives
    word = generate_blank_words()  # Generate the blank word and target word
    blank_word = word[0]  # List of underscores representing the word
    target_word = word[1]  # List of characters in the word

    # Display the starting Hangman banner
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
    \n\n''')

    # Main game loop
    while remain_life > 0:

        # Display the current status of the word with blanks
        print(f'remain words: {''.join(blank_word)}\n')

        # Get the player's guess
        guessed_char = input("guess the word: ")

        # Check if the guessed character exists in the target word
        is_char_exists = [index for index, char in enumerate(target_word) if char == guessed_char]

        if is_char_exists:
            # If the guessed character is in the word, reveal it in the blank word
            for index in is_char_exists:
                blank_word[index] = target_word[index]
            
            current_word = ''.join(blank_word)  # Combine the current blanks to form a word string

            if current_word == ''.join(target_word):
                # If the player successfully guesses the word, end the game with a win message
                print("Congratulations! You've won!")
                print(f"The word is: {current_word}")
                break
        else:
            # If the guess is wrong, reduce the player's remaining lives
            print("Wrong guess!\n")
            print(icons[remain_life])  # Display the corresponding hangman icon
            remain_life -= 1  # Decrement life by 1

            if(remain_life == 0):
                # If the player runs out of lives, display the full hangman and end the game with a loss message
                print(icons[remain_life])
                print("Game Over!")
                print(f"The correct word was: {''.join(target_word)}")

# Run the game                   
run_hangman()

