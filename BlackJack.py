import random
import os
from typing import List, Any

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
lst_user_cards = []
lst_computer_cards = []

while True:

    # Check to see if user has blackjack if yes they win
    # Inside calculate_score() check for an 11 (ace).
    # If the score is already over 21, remove the 11 and replace it with a 1.
    def calculate_player_score(user_cards):
        if sum(user_cards) == 21 and len(user_cards) == 2:
            return 0
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
            return sum(user_cards)
        else:
            return sum(user_cards)

    # Calculates the computer score and returns the sum
    def calculate_comp_score(computer_cards):
        if sum(computer_cards) == 21 and len(computer_cards) == 2:
            return 0
        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
            return sum(computer_cards)
        else:
            return sum(computer_cards)

    # Uses the List below to return a random card.
    # 11 is the Ace.
    # Deal the user and computer 2 cards each
    def deal_card(card):
        # Returns a random card from the deck
        card = random.choice(cards)
        return card

    # Created a function called compare() that passes in the user_score and computer_score.
    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0),
    # then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("Draw")
        if user_score == 0:
            print("You Win")
        elif computer_score == 0:
            print("You Lose")
        elif user_score > 21:
            print("You Lose")
        elif computer_score > 21:
            print("You Win")
        else:
            return

    # User draws card
    # Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.

    # If the game has not ended, ask the user if they want to draw another card.
    # If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # The score will need to be rechecked with every new card drawn
    # and the checks need to be repeated until the game ends.
    def draw_cards(sum_of_user_cards, sum_of_comp_cards):
        while sum_of_user_cards < 21 and sum_of_user_cards != 0 and sum_of_comp_cards < 21 and sum_of_comp_cards != 0:
            print(f"Your cards: {lst_user_cards}")
            print(f"Player score: {get_player_score}")
            draw_another_card = input("Do you want to draw another card? Input Y for yes or N for no: ")
            if draw_another_card == "Y".lower():
                add_user_card = deal_card(lst_user_cards)
                lst_user_cards.append(add_user_card)
                print(f"Your cards: {lst_user_cards}")
                sum_of_user_cards = sum(lst_user_cards)
                print(f"Player Score: {sum_of_user_cards}")
                compare(sum_of_user_cards, sum_of_comp_cards)

            if sum_of_comp_cards < 17:
                add_comp_card = deal_card(lst_computer_cards)
                lst_computer_cards.append(add_comp_card)
                print(f"Computer cards: {lst_computer_cards}")
                sum_of_comp_cards = sum(lst_computer_cards)
                print(f"Computer Score: {sum_of_comp_cards}")
                compare(sum_of_user_cards, sum_of_comp_cards)
            else:
                break

    for i in range(2):
        lst_user_cards.append(deal_card(lst_user_cards))
        lst_computer_cards.append(deal_card(lst_computer_cards))

    # Call Functions
    deal_card(lst_user_cards)
    get_player_score = calculate_player_score(lst_user_cards)
    get_comp_score = calculate_comp_score(lst_computer_cards)
    draw_cards(get_player_score, get_comp_score)

    # Ask the user if they want to restart the game.
    # If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    user_input = input("Do you want to restart the game? Type Y for yes or N for no: ")
    if user_input == "Y".lower():
        continue
    break