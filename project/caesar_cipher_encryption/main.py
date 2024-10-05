import art
print(art.logo)

def caesar_cipher(message, key, encode_or_decode):
    """
    Encrypts or decrypts a message using the Caesar cipher method.

    The Caesar cipher is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number 
    of places down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 
    'C', and so on.

    Parameters:
        message (str): The input message to be encrypted or decrypted.
        key (int): The number of positions to shift each letter in the message.
        encode_or_decode (str): A string indicating whether to 'encode' or 'decode' the message.
                                It should be either 'encode' or 'decode'.

    Returns:
        str: The encrypted or decrypted message, prefixed with either 'Encrypted message:' or 'Decrypted message:'.
    """
    compiled_message = ""  # Initialize an empty string to hold the resulting message
    splitted_message = list(message)  # Split the message into a list of characters
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  # List of lowercase alphabet characters

    for char in splitted_message:
        # Check if the character is a letter (case insensitive)
        if char.lower() in chars:
            index = chars.index(char.lower())  # Find the index of the character in the chars list
            
            # Determine the shift value based on whether we're encoding or decoding
            shift = key if encode_or_decode == 'encode' else -key
            
            # Calculate the new character index and wrap around using modulo
            indices_char = chars[(index + shift) % len(chars)]
            
            # Preserve the case of the original character
            if char.isupper():
                compiled_message += indices_char.upper()  # Add the uppercase character to the compiled message
            else:
                compiled_message += indices_char  # Add the lowercase character to the compiled message
        
        else:
            compiled_message += char  # If it's not a letter, add it unchanged to the compiled message

    # Return the compiled message with appropriate prefix
    return f'Encrypted message: {compiled_message}' if encode_or_decode == 'encode' else f'Decrypted message: {compiled_message}'


def main():
    """
    Main function to run the Caesar cipher program.
    
    This function prompts the user for input regarding the operation they wish to perform (encode or decode),
    the message they want to process, and the shift value. It continuously allows the user to encode or decode 
    messages until they decide to stop the program.

    Workflow:
    - The user is asked to specify whether they want to encode or decode a message.
    - The user inputs their message.
    - The user specifies the shift number, which determines how many positions each letter in the message 
      will be shifted.
    - The program calls the caesar_cipher function to perform the encryption or decryption.
    - The user is prompted to restart the program or exit.

    If the user inputs 'no' when asked to restart, the program will terminate.
    """
    
    RESTART_PROGRAM = True  # Flag to control the program loop

    while RESTART_PROGRAM:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")  # Get user input for direction
        message = input("Type your message: \n")  # Get the message to process
        key = int(input("Type the shift number: \n"))  # Get the shift value

        # Call the caesar_cipher function and print the result
        result = caesar_cipher(message, key, direction)
        print(result, "\n")  # Display the encrypted or decrypted message
        restart = input("Wanna restart the program? Type 'yes' if want to restart, 'no' for stop the program. \n")

        if restart.lower() == 'no':
            RESTART_PROGRAM = False  # Exit the loop and terminate the program

# Execute the main function
main()