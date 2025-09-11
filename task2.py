import random
from itertools import product


values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 11
}

def create_deck():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    cards=list(product(ranks,suits,repeat=1))
    random.shuffle(cards)

    return cards

def score(hand):
    return sum(values[card]  for card,rank in hand)



def play():

    cards=create_deck()

    player = [cards.pop(),cards.pop()]
    computer = [cards.pop(),cards.pop()]

    print(f"Player hand : {player}      Score : {score(player)}")
    print(f"Computer hand : {computer}    Score : {score(computer)}")

    while True:
        choice=input("Do you want to 'add' or 'stop'? ")

        if choice=='stop':
            break
        else:
            player.append(cards.pop())
            print(f"Player hand : {player}      Score : {score(player)}")
            if score(player)>21:
                print('You Lose')
                return
            
    while score(computer)<17:
        computer.append(cards.pop())
        print(f"Computer hand : {computer}    Score : {score(computer)}")
        if score(computer)>21:
            print('Player Wins')
            return
    
    player_score=score(player)
    computer_score=score(computer)

    if computer_score>player_score:
        print('Computer Wins')
    elif player_score>computer_score:
        print("Player Wins")
    else:
        print("Tie")


play()