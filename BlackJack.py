import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
lst_user_cards = []
lst_computer_cards = []
#Create a function called calculate_score() that takes a List of cards as input and returns the score. 
#Check to see if user has blackjack if yes they win
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_player_score(user_cards):
    if sum(user_cards) == 21 and len(user_cards) == 2:
        return 0
    if 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)  
        return sum(user_cards)
    else:
        return sum(user_cards)
        
def calculate_comp_score(computer_cards):
    if sum(computer_cards) == 21 and len(computer_cards) == 2:
        return 0   
    if 11 in computer_cards and sum(computer_cards) > 21:
        computer_cards.remove(11)
        computer_cards.append(1)
        return sum(computer_cards)
    else:
        return sum(computer_cards)
        
#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.  
#Deal the user and computer 2 cards each using deal_card() and append().
def deal_card(card):
    # Returns a random card from the deck
    card = random.choice(cards)
    return card 
    
for i in range(2):
    lst_user_cards.append(deal_card(lst_user_cards))
    lst_computer_cards.append(deal_card(lst_computer_cards))

deal_card(lst_user_cards)
#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
get_player_score = calculate_player_score(lst_user_cards)
get_comp_score = calculate_comp_score(lst_computer_cards)

if get_player_score == 0:
    print("You Lose")
elif get_comp_score == 0:
    print("You Win")
if get_player_score > 21:
    print("You Lose")
elif get_comp_score > 21:
    print("You Win")

print(f"Player score: {lst_user_cards}")
print(f"Computer score: {lst_computer_cards}")
print(f"Player score: {get_player_score}")
print(f"Computer score: {get_comp_score}")


