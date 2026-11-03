import random
import art
print(art.logo)

# difficulty levels shows number of attempts
difficulty_levels = {
    "easy": 10,
    "hard": 5,
}
# computer picks a random number between 1 and 100 (including 1 and 100)
computer_chosen = random.randint(1, 100)

# game starts
print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

# user picks difficulty level
level = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

# ask user to guess number based on difficulty level
for attempt in range(difficulty_levels[level], 0, -1): # range going down in reverse

    print(f"You have {attempt} attempt(s) remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == computer_chosen: # if user guessed right, stop game
        print(f"You got it! The answer was {guess}")
        break
    elif guess < computer_chosen: # give clues otherwise
        print("Too low.")
    elif guess > computer_chosen:
        print("Too high.")

    # if not last attempt ask to guess again
    if attempt != 1:
        print("Guess again")
    else:  # incase not guessed through all the attempts - restart game with different number
        print("You have run out of guesses. Refresh page to start again.")
