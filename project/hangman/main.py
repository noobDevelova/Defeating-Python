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
    random_words = ['mouse', 'walking', 'jealous', 'sitting']
    word = random_words[random.randint(0, len(random_words) - 1)]
    return word

def generate_blank_words():
    generated_word = generate_random_words()
    separated_word = list(generated_word)
    blanks = list('_' * len(separated_word))
    return [blanks, separated_word]

def run_hangman():
    MAX_LIFE = 6
    remain_life = 6
    word = generate_blank_words()
    blank_word = word[0]
    target_word = word[1]

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

    while remain_life > 0:
        print(f'remain words: {''.join(blank_word)}\n')
        guessed_char = input("guess the word: ")
        is_char_exists = [index for index, char in enumerate(target_word) if char == guessed_char]

        if is_char_exists:
            for index in is_char_exists:
                blank_word[index] = target_word[index]
            
            current_word = ''.join(blank_word)

            if current_word == ''.join(target_word):
                print("Congratulations! You've won!")
                print(f"The word is: {current_word}")
                break
        else:
            print("Wrong guess!\n")
            print(icons[remain_life])
            remain_life -= 1

            if(remain_life == 0):
                print(icons[remain_life])
                print("Game Over!")
                print(f"The correct word was: {''.join(target_word)}")
                    
run_hangman()

