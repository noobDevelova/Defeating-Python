import art

def auction(bidders):
    """
    Determines the winner of the auction based on the highest bid.

    Args:
        bidders (dict): A dictionary where the key is the name of the bidder 
                        and the value is their bid amount.

    Returns:
        str: The name of the bidder with the highest bid.
    """
    # Initialize with the first bidder as the highest bid reference.
    highest = next(iter(bidders))

    # Iterate through all bidders to find the highest bid.
    for bidder in bidders:
        if bidders[bidder] > bidders[highest]:
            highest = bidder  # Update highest if a higher bid is found.

    return highest  # Return the name of the highest bidder.

def main():
    """
    Main function to handle the auction flow. 
    Collects name and bid amount from each participant and announces the winner.
    """
    BID_STILL_GOING = True  # Control variable to continue or stop the auction.
    bidder = {}  # Dictionary to store bidder names and their bids.

    print(art.logo)  # Display the auction logo.

    # Loop until there are no more bidders.
    while BID_STILL_GOING:
        # Get the name and bid amount from each bidder.
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))

        # Store the bidder's information.
        bidder[name] = bid
        
        # Ask if there are other bidders.
        other_bidder = input("Is there any other bidders? Type 'yes' or 'no'.\n")

        # If no other bidders, exit the loop and print the results.
        if other_bidder.lower() == 'no':
            BID_STILL_GOING = False
            highest_bidder = auction(bidder)  # Determine the highest bidder.
            
            # Clear the screen for a clean output.
            print('\n' * 20)
            
            # Announce the winner and their bid amount.
            print(f'The winner is {highest_bidder} with a bid of ${bidder[highest_bidder]}.')
            
        # If there are still other bidders, clear the screen and continue.
        elif other_bidder.lower() == 'yes':
            # Clear the screen before the next bidder.
            print('\n' * 20)

# Start the main function.
main()