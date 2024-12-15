# Import the P1Random class from the p1_random module.
from p1_random import P1Random

# Create an instance of the P1Random class to generate random numbers.
rng = P1Random()

# Initialize various game-related variables.
user_input = 1              # User input placeholder
game_number = 1            # Tracks the current game number
winning_player = 0         # Tracks the number of times the player wins
winning_dealer = 0         # Tracks the number of times the dealer wins
game_ties = 0              # Tracks the number of tie games
total_games = 0            # Tracks the total number of games played

# Define a function to get a random playing card.
def getOneCard():
    # Generate a random card number between 1 and 13.
    card_number = rng.next_int(13) + 1
    card_value = 0

    # Determine the card's value based on its number.
    if card_number == 13:
        print("\nYour card is a KING!")
        card_value = 10
    elif card_number == 12:
        print("\nYour card is a QUEEN!")
        card_value = 10
    elif card_number == 11:
        print("\nYour card is a JACK!")
        card_value = 10
    elif card_number == 1:
        print("\nYour card is a ACE!")
        card_value = 1
    else:
        print(f"\nYour card is a {card_number}!")
        card_value = card_number   
    return card_value 

# Start the game loop.
while user_input != "4":
   
    print(f"START GAME #{game_number}")
    game_number += 1    

    hand_play = 0           # Initialize the player's hand value
    dealer_hand = 0         # Initialize the dealer's hand value
    card_value = getOneCard()  # Get the value of the first card drawn
    hand_play += card_value  # Update the player's hand value
    print(f"Your hand is: {hand_play}\n")

    current_round = True  # Set a flag to indicate that the current game round is ongoing

    # Start a sub-loop for the current game round.
    while current_round:
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")

        user_input = input("Choose an option: ")

        # Process the user's input.
        if user_input == "1": 
            card_value = getOneCard() # Get the value of the next card drawn
            hand_play += card_value # Update the player's hand value
            print(f"Your hand is: {hand_play}\n")

            if hand_play > 21: # Check if the player's hand value exceeds 21
                print("You exceeded 21! You lose.\n")
                winning_dealer += 1 # Increment the dealer's win counter
                current_round = False # Set the flag to indicate that the current game round is over
            elif hand_play == 21: # Check if the player's hand value is 21
                print("BLACKJACK! You win!\n")
                winning_player += 1 # Increment the player's win counter
                current_round = False
        elif user_input == "2": 
            dealer_hand = rng.next_int(11) + 16 # Generate a random number between 16 and 26
            print(f"Dealer's hand: {dealer_hand}") # Print the dealer's hand value
            print(f"Your hand is: {hand_play}\n")    

            if dealer_hand > 21 or dealer_hand < hand_play: # Check if the dealer's hand value exceeds 21 or is less than the player's hand value
                print("You win!\n")
                winning_player += 1 # Increment the player's win counter
            elif dealer_hand == hand_play: # Check if the dealer's hand value is equal to the player's hand value
                print("It's a tie! No one wins!\n")
                game_ties += 1 # Increment the tie game counter
            else:
                print("Dealer wins!\n")
                winning_dealer += 1 # Increment the dealer's win counter
            current_round = False
        elif user_input == "3": # Check if the user wants to print the game statistics
            print(f"Number of Player wins: {winning_player}") # Print the number of times the player wins
            print(f"Number of Dealer wins: {winning_dealer}") # Print the number of times the dealer wins
            print(f"Number of tie games: {game_ties}") # Print the number of tie games
            print(f"Total # of games played is: {total_games}") # Print the total number of games played
            if total_games > 0: # Check if the total number of games played is greater than 0
                print(f"Percentage of Player wins: {winning_player / total_games * 100:.1f}%\n") # Print the percentage of times the player wins
        elif user_input == "4": # Check if the user wants to exit the program
            current_round = False
        else:
            print("\nInvalid input!\nPlease enter an integer value between 1 and 4.\n")

    # Increment the total games counter.
    total_games += 1
