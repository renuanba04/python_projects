import random
import art

new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while new_game == 'y':

    print("\n" * 20)
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # deal both user and computer a starting hand of two card values
    user_cards = random.choices(cards, k = 2)
    computer_cards = random.choices(cards, k = 2)

    def print_final_stats(player, dealt_cards, score):
        print(f"{player.title()}'s final hand: {dealt_cards}, final score: {score}")

    blackjack_cards = [10, 11]
    if sorted(computer_cards) == blackjack_cards:

        print_final_stats("user", user_cards, sum(user_cards))
        print_final_stats("computer", computer_cards, sum(computer_cards))
        print("Computer Wins with a BlackJack.")

    elif sorted(user_cards) == blackjack_cards:
        print_final_stats("user", user_cards, sum(user_cards))
        print_final_stats("computer", computer_cards, sum(computer_cards))
        print("Win with a BlackJack")

    else:
        deal_cards = True
        while deal_cards:

            user_score = sum(user_cards)
            computer_score = sum(computer_cards)

            if [11] in user_cards and user_score > 21:
                user_score -= 10
            elif [11] in computer_cards and computer_score > 21:
                computer_score -= 10

            if user_score < 21:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                deal = input("Type 'y' to get another card, type 'n', to pass: ").lower()
                if deal == 'y':
                    user_cards.append(random.choice(cards))
                    continue
                else:
                    while computer_score < 17:
                        computer_cards.append(random.choice(cards))
                        computer_score = sum(computer_cards)

                    if computer_score > 21:
                        print_final_stats("user", user_cards, user_score)
                        print_final_stats("computer", computer_cards, computer_score)
                        print("Opponent went over. You Win.")

                    elif user_score > computer_score:
                        print_final_stats("user", user_cards, user_score)
                        print_final_stats("computer", computer_cards, computer_score)
                        print("You win.")

                    elif user_score == computer_score:
                        print_final_stats("user", user_cards, user_score)
                        print_final_stats("computer", computer_cards, computer_score)
                        print("Draw.")

                    else:
                        print_final_stats("user", user_cards, user_score)
                        print_final_stats("computer", computer_cards, computer_score)
                        print("You lose.")

                    deal_cards = False
            else:
                print_final_stats("user", user_cards, user_score)
                print_final_stats("computer", computer_cards, computer_score)
                print("You went over. You lose.")
                deal_cards = False

    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()