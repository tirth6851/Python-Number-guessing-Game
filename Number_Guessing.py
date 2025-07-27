import random
import time



def main():
    """Run the game and ask the player if they want to play again."""
    start_game()
    while ask_to_play():
        check_winner()
    print("Maybe next time!")



def start_game():
    """Display the introduction text for the game."""
    print("Loading...")
    time.sleep(2)
    print("Welcome to the Number Guessing Game!")
    time.sleep(1)
    print("I'm thinking of a number between 1 and 10.")
    time.sleep(1)
    print("You have 3 attempts to guess it.")
    time.sleep(1)



def ask_to_play():
    """Prompt the player to start or replay the game."""
    start_game_choice = input("Ready to play? (yes/no): ").lower()
    return start_game_choice == "yes"


def computer_guess():
    """Return a random integer between 1 and 10."""
    return random.randint(1, 10)


def player_guess():
    """Prompt the player to guess a number and validate the input."""
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")



def check_winner():
    """Run the guessing logic and report the outcome."""
    secret_number = computer_guess()
    for attempt in range(1, 4):
        guess = player_guess()
        if guess == secret_number:
            print("You win!")
            print("You guessed the correct number!")
            return
        else:
            if attempt == 3:
                hint = [secret_number]
                if secret_number - 1 >= 1:
                    hint.append(secret_number - 1)
                if secret_number + 1 <= 10:
                    hint.append(secret_number + 1)
                random.shuffle(hint)  
                print(f"Hint! The number is one of these: {hint}")
                final_guess = player_guess()
                if final_guess == secret_number:
                    print("You win! You guessed the correct number!")
                else:
                    print("You lose the game!")
                    print(f"The correct number was {secret_number}")
                return
            else:
                print(f"Wrong guess! Try again. Attempts left: {3 - attempt}")





if __name__ == "__main__":
  main()
