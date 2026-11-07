from random import choice
import art
from game_data import data

SCORE = 0

def random_celebrity():
    """Returns celebrity details as a dictionary"""
    return choice(data)

def display(a_details, b_details):
    """Displays Celeb A vs Celeb B in a cool fashion"""
    print(f"Compare A: {a_details["name"]}, a {a_details["description"]}, from {a_details["country"]}")
    print(art.vs)
    print(f"Against B: {b_details["name"]}, a {b_details["description"]}, from {b_details["country"]}")

def check_answer(a_followers, b_followers, guess):
    """Takes user's guess, followers' count and returns whether the guess is right"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

def game():
    """Higher or Lower Game for Instagram Followers"""
    global SCORE
    print(art.logo)
    b = random_celebrity()
    should_game_continue = True
    while should_game_continue:

        a = b
        b = random_celebrity()
        display(a, b)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_right = check_answer(a["follower_count"], b["follower_count"], guess)
        print("\n" * 20)
        print(art.logo)

        if is_right:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            should_game_continue = False

# Start game here
game()
