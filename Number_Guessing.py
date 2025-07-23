import random
import time

def main():
  start_game()


def start_game():
  print(f"Loading... {time.sleep(5)}")
  print("Welcome to the Number Guessing Game!")
  time.sleep(1)
  print("I'm thinking of a number between 1 and 10.")
  time.sleep(1)
  print("You have 3 attempts to guess it.")
  time.sleep(1)
  return input("ready to play?")

def C_guess():
  return random.randint(1,10)

def P_guess():
  return int(input("Guess a number between 1 and 10: "))

def check_winner():
  if P_guess() == C_guess():
    print("You win!")
  else:
    print("You lose!")
    time.sleep(1)








#burn out 