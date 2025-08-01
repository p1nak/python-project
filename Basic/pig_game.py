import random

def roll():
    roll = random.randint(1, 6)
    return roll

while True:
    Players = input("Enter the number of players (2-4): ")
    if Players in ['2', '3', '4']:
        Players = int(Players)
        break
    print("Invalid input. Please enter a number between 2 and 4.")

while True:
    try:
        max_score = int(input("Enter the maximum score to win the game (By Default 50): ") )
        if max_score > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

player_scores = [0] * Players
while max(player_scores) < max_score:
    for player_index in range(Players):
        print(f"\nPlayer {player_index + 1}'s turn.")
        current_score = 0

        while True:   
            again = input("Do you want to roll the dice? (y or " "): ")
            if again.lower() == 'n':
                print("Game ended.")
                break
            value = roll()
            print(f"You rolled a {value}.")
            if value == 1:
                print("You rolled a 1. Your turn ends and you lose all points for this turn.")
                current_score = 0
            else:
                current_score += value
                print(f"Current score for this turn: {current_score}")
            
            if current_score >= max_score:
                break

        player_scores[player_index] += current_score
        print(f"your total score is now {player_scores[player_index]}.")

        if player_scores[player_index] >= max_score:
            print(f"\n🎉 Player {player_index + 1} wins with {player_scores[player_index]} points! 🎉")
            break
    else:
        continue
    break
