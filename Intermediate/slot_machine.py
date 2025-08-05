import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 10:
                return amount
            else:
                print("Amount must be greater than $10")
        else:
            print("Please enter a number!")

def get_the_number_of_line():
    while True:
        line = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                return line
            else:
                print("Enter a valid line number")
        else:
            print("Please enter a number!")

def get_bet(balance):
    while True:
        bet = input(f"Enter the amount to bet on each line (balance: ${balance}): $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                if bet <= balance:
                    return bet
                else:
                    print("You don't have enough balance.")
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number!")

def spin_the_wheel(line, bet):
    Random_line = random.randint(1, MAX_LINES)
    print(f"Wheel stopped at line {Random_line}")
    if Random_line == line:
        print("You guessed the correct line 🎉")
        return bet * 5 
    else:
        print("You lost!")
        return 0

def main():
    balance = deposit()

    while balance >= MIN_BET:
        line = get_the_number_of_line()
        bet = get_bet(balance)

        spin = input("Do you want to spin the wheel? (yes/no): ").lower()
        if spin != "yes":
            print("Goodbye!")
            break

        winnings = spin_the_wheel(line, bet)
        balance -= bet
        balance += winnings

        print(f"Your current balance is: ${balance}")
        if balance < MIN_BET:
            print("You don't have enough balance to continue.")
            break

        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            break

main()
