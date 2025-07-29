import random

def roll_dice():
    """Simulates rolling a single six-sided die."""
    return random.randint(1, 6)

def main():
    """Main function to run the dice rolling simulator."""
    while True:
        input("Press Enter to roll the dice (or type 'quit' to exit): ")
        user_input = input().lower() # Read user input after pressing Enter

        if user_input == 'quit':
            print("Exiting the dice rolling simulator. Goodbye!")
            break
        else:
            result = roll_dice()
            print(f"You rolled a: {result}")

if __name__ == "__main__":
    main()
