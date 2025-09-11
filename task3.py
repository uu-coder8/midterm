import logging


logging.basicConfig(
    filename="atm_log.log", 
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

balance=2000

def check_balance():
    logging.info(f"Balance Check {balance}")
    print(f"Balance : {balance}")
    

def deposit(num):
    global balance
    if num>1000:
        print("Max limit is 1000")
    else:
        balance+=num
        logging.info(f"Deposited {num} GEL   New balance: {balance} GEL")
        print(f"Deposited {num} GEL")

def withdraw(num):
    global balance
    if num>balance:
        print('You dont have enough balance')
    else:
        balance-=num
        logging.info(f"Withdrew {num} GEL   New balance: {balance} GEL")
        print(f"Withdrew {num} GEL")


def main():
    global balance

    while True:
        print()
        print('Choices : ')
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print()

        choice=int(input('Your choice : '))
        match choice:
            case 1:
                check_balance()
            case 2:
                n=int(input('Enter amount (GEL) : '))
                deposit(n)
            case 3:
                n=int(input('Enter amount (GEL) : '))
                withdraw(n)
            case 4:
                logging.info(f"Exit")
                break
main()