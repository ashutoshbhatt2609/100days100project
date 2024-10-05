from art import logo
import random
import os 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def cal_score(cards):
    """Takes a list and returns the sum of the elements in the list."""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score,com_score):
    if user_score==com_score:
        return "Draw"
    elif com_score==0:
        return "Lose, the oppent has Blackjack!!!!!!"
    elif user_score==0:
        return "Win, You have Blackjack!!!!!"
    elif user_score>21:
        return "You went over. You lose!!!"
    elif com_score>21:
        return "Opponent went over. You won!!!"
    elif user_score>com_score:
        return "You win!!!!!!1"
    else:
        return "You lose!!!!"
def deal_card():
    """Returns a random card from deck."""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def play_game():
    print(logo)
    user_card=[]
    com_card=[]
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_card())
        com_card.append(deal_card())
    while not is_game_over:
        user_score=cal_score(user_card)
        com_score=cal_score(com_card)

        print(f"Your card: {user_card} ,Current score: {user_score}")
        print(f"Computer's First Card:{com_card[0]}")

        if user_score==0 or com_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should=='y':
                user_card.append(deal_card())
            else:
                is_game_over=True

    while com_score!=0 and com_score<17:
        com_card.append(deal_card())
        com_score=cal_score(com_card)

    print(compare(user_score,com_score))


while input("Do you want to play a game of blackjack ? Type 'y' or 'n':-")=='y':
    cls()
    play_game()
    




