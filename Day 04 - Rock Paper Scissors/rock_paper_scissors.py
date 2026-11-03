import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_options = [rock, paper, scissors]

user_choice_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip())
if 0 <= user_choice_index < len(game_options):

    user_choice = game_options[user_choice_index]
    print(user_choice)
    computer_choice = random.choice(game_options)
    print("Computer chose:")
    print(computer_choice)

    if user_choice == computer_choice:
        print("It's a draw")

    elif (user_choice == rock and computer_choice == paper) or \
         (user_choice == paper and computer_choice == scissors) or \
         (user_choice == scissors and computer_choice == rock):
        print("You lose")

    elif (user_choice == rock and computer_choice == scissors) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissors and computer_choice == paper):
        print("You win!")

    else:
        print("Unknown Combination")

else:
    print("You typed an invalid number, you lose!")
