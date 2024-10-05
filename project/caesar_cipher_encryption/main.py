def caesar_cipher(message, key, encode_or_decode):
    """
    Encrypts or decrypts a message using the Caesar cipher method.

    Parameters:
        message (str): The input message to be encrypted or decrypted.
        key (int): The number of positions to shift each letter in the message.
        encode_or_decode (str): A string indicating whether to 'encode' or 'decode' the message.

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
    Prompts the user for input and calls the caesar_cipher function to process the input.
    """
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")  # Get user input for direction
    message = input("Type your message: \n")  # Get the message to process
    key = int(input("Type the shift number: \n"))  # Get the shift value

    # Call the caesar_cipher function and print the result
    result = caesar_cipher(message, key, direction)
    print(result)

# Execute the main function
main()