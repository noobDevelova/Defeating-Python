import random
import art

def get_random_stack():
    """
    Returns a random card value from a standard deck of Blackjack.
    
    The card stack consists of the values: 11 (Ace), 2-10, and the face cards 
    (King, Queen, Jack) which are represented by 10.
    
    Returns:
        int: A randomly selected card value.
    """
    card_stack = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_stack)

def get_user_data():
    """
    Generates a new hand for the user with two randomly selected cards.
    
    Returns:
        dict: A dictionary containing the user's hand with two card values.
    """
    data = {
        'stack': [get_random_stack(), get_random_stack()]
    }
    return data

def get_computer_data():
    """
    Generates a new hand for the computer with two randomly selected cards.
    
    Returns:
        dict: A dictionary containing the computer's hand with two card values.
    """
    data = {
        'stack': [get_random_stack(), get_random_stack()]
    }
    return data

def blackjack():
    """
    Implements the main logic for the Blackjack game.
    
    - The user is dealt two cards, and their total is calculated.
    - The computer is also dealt two cards, but only one card is shown initially.
    - The user has the option to take additional cards (hit) or stop (pass).
    - The computer must take additional cards if their total score is less than 17.
    - The winner is determined based on the final hand scores.
    - If the user or computer exceeds 21 points, they lose automatically.
    """

    print(art.logo)

    user_data = get_user_data()
    computer_data = get_computer_data()

    user_score = sum(user_data['stack'])
    computer_score = sum(computer_data['stack'])

    print(f"Your cards: {user_data['stack']}, current score: {user_score}")
    print(f"Computer's first card: {computer_data['stack'][0]}")

    # Check if user has a natural Blackjack (21 points)
    if user_score == 21:
        print(f"Your final hand: {user_data['stack']}, final score: {user_score}")
        print(f"Computer's final hand: {computer_data['stack']}, final score: {computer_score}")
        print("Win with a Blackjack 😎")
        return

    # Allow the user to draw additional cards if the score is less than 21
    while user_score < 21:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if get_another_card == 'y':
            user_data['stack'].append(get_random_stack())
            user_score = sum(user_data['stack'])
            print(f"Your cards: {user_data['stack']}, current score: {user_score}")
            print(f"Computer's first card: {computer_data['stack'][0]}")
            
            # Check if user went over 21
            if user_score > 21:
                print(f"Your final hand: {user_data['stack']}, final score: {user_score}")
                print(f"Computer's final hand: {computer_data['stack']}, final score: {computer_score}")
                print("You went over 21. You lose 😭")
                return
        else:
            break
    
    # Computer will draw cards until its score is at least 17
    while computer_score < 17:
        computer_data['stack'].append(get_random_stack())
        computer_score = sum(computer_data['stack'])

    print(f"Your final hand: {user_data['stack']}, final score: {user_score}")
    print(f"Computer's final hand: {computer_data['stack']}, final score: {computer_score}")

    # Determine the winner based on final scores
    if computer_score > 21:
        print("Computer went over 21. You win! 😃")
    elif user_score > computer_score:
        print("You win! 😃")
    elif user_score < computer_score:
        print("You lose 😭")
    else:
        print("It's a draw!")

def main():
    """
    Main loop to control the flow of the game.
    
    The user is prompted to start a new game of Blackjack. If the user chooses 
    to play, the `blackjack` function is called. Otherwise, the game loop exits.
    """
    WANNA_PLAY = True
    
    while WANNA_PLAY:
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        
        if play_game == 'y':
            blackjack()
        else:
            WANNA_PLAY = False

# Start the Blackjack game
main()
