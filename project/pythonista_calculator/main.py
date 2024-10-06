import art  # Importing the art module to display a logo or ASCII art.

def add(n1, n2):
    """Add two numbers.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The sum of n1 and n2.
    """
    return n1 + n2

def subtract(n1, n2):
    """Subtract the second number from the first number.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The result of n1 minus n2.
    """
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers.

    Args:
        n1 (float): The first number.
        n2 (float): The second number.

    Returns:
        float: The product of n1 and n2.
    """
    return n1 * n2

def division(n1, n2):
    """Divide the first number by the second number.

    Args:
        n1 (float): The numerator.
        n2 (float): The denominator.

    Returns:
        float: The result of n1 divided by n2.
    """
    return n1 / n2

def get_operator():
    """Get a dictionary of available operations.

    Returns:
        dict: A dictionary mapping operation symbols to their corresponding functions.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": division
    }
    return operations

def operate(first_num, operator, next_num):
    """Perform the specified operation on two numbers.

    Args:
        first_num (float): The first number.
        operator (str): The operation to perform.
        next_num (float): The second number.

    Returns:
        float: The result of the operation.
    """
    list_operator = get_operator()
    return list_operator[operator](first_num, next_num)

def calculate():
    """Main function to handle user input and perform calculations interactively."""
    print(art.logo)  # Display the logo or ASCII art.

    STILL_CONTINUE = True  # Flag to control the main calculation loop.
    first_num = float(input("What's the first number?: "))  # Get the first number.
    operator = get_operator()  # Get available operations.

    while STILL_CONTINUE:
        for symbols in operator: 
            print(symbols)  # Display available operations.

        operation = input("Pick an operation: ")  # Get the chosen operation.

        next_num = float(input("What's the next number?: "))  # Get the next number.
        result = operate(first_num, operation, next_num)  # Perform the operation.
        print(f'{first_num} {operation} {next_num} = {result}')  # Display the result.

        IS_CONTINUE = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        
        if IS_CONTINUE.lower() == 'y':
            first_num = result  # Update first_num to the result for further calculations.
        else:
            STILL_CONTINUE = False  # Exit the loop.
            print("\n" * 20)  # Clear the console for a fresh start.
            calculate()  # Start a new calculation session.

# Start the calculator by calling the calculate function.
calculate()