import random
import logging

logging.basicConfig(
    filename="lottery.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

jackpot=10_000_000

def win_amount(matches):
    match matches:
        case 6:
            return jackpot
        case 5:
            return int(jackpot*0.6)
        case 4:
            return int(jackpot*0.4)
        case 3:
            return int(jackpot*0.2)
        case _:
            return 0


def play():
    
    lottery_numbers=sorted(random.sample(range(1,50),6))
    print('Winning numbers : ',*lottery_numbers)

    print("Enter your 6 numbers (from 1 to 49):")
    players_nums=[]
    for i in range(1,7):
        num=int(input(f"Enter Number {i} : "))
        players_nums.append(num)
    
    matches=len(set(lottery_numbers)&set(players_nums))
    prize_amount=win_amount(matches)

    print("Winning Numbers : ",*lottery_numbers)
    print("Player Numbers : ",*players_nums)
    print(f'Matches : {matches}')

    if prize_amount>0:
        print(f"You have won : {prize_amount:_}")
    else:
        print("You loser")
    
    logging.info(f"Winning numbers: {lottery_numbers} | "
        f"Player numbers: {players_nums} | "
        f"Matches: {matches} | "
        f"Prize Amount: {prize_amount}")

play()