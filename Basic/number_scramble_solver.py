import random

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (2 digits)")
    print("2. Medium (3 digits)")
    print("3. Hard (4 digits)")
    
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            return 2
        elif choice == '2':
            return 3
        elif choice == '3':
            return 4
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")



def check(guess, original_number):
    if not guess.isdigit() or len(guess) != len(original_number):
        print("⚠️ The number is invalid! Enter only digits of correct length.")
        return False

    for i, digit in enumerate(guess):
        if digit == original_number[i]:
            print(f"✅ {digit} is correct and in the right place.")
        elif digit in original_number:
            print(f"🔁 {digit} is in the number but in the wrong place.")
        else:
            print(f"❌ {digit} is not in the number.")
    return True


def main():
    digit_count = choose_difficulty()

    original_digits = random.sample(range(0, 10), digit_count)
    original_number = ''.join(map(str, original_digits))


    scrambled = original_digits[:]
    random.shuffle(scrambled)
    print("🔀 Scrambled digits:", scrambled)    

    attempts = 0
    while True:
        guess = input("🔢 Your guess: ").strip()
        attempts += 1

        if not check(guess, original_number):
            continue

        if guess == original_number:
            print(f"\n🎉 Correct! You solved it in {attempts} attempts.")
            break

# Step 5: Run the game
if __name__ == "__main__":
    main()
