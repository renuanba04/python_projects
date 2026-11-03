from queue import PriorityQueue
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
ANSWER = randint(1, 100)

# function to set difficulty
def set_difficulty(choice):
    if choice == "easy":
        return EASY_LEVEL_TURNS
    elif choice == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Incorrect choice.")
        return 0

# function to check the guess
def check_answer(guess, attempts):
    if guess < ANSWER:
        print("Too low")
        return attempts - 1
    elif guess > ANSWER:
        print("Too high")
        return attempts - 1
    else:
        print(f"You got it! The answer was {guess}")
        return 0

# function for the game
def play_game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_difficulty(difficulty)

    while attempts != 0:

        print(f"You have {attempts} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, attempts)

        if attempts != 0:
            print("Guess again")
        else:
            print("You have run out of guesses. Try again")

play_game()