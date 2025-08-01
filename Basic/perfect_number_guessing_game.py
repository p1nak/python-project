import random

# Input the range for the random number
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Generate a random number within the range
random_number = random.randint(start, end)

guesses = 0
guess = None

print(f"\n🎯 Guess the number between {start} and {end}!")

# Loop until the user guesses correctly
while guess != random_number:
    try:
        guess = int(input("🤔 Your guess: "))
        guesses += 1

        if guess < random_number:
            print("🔼 Higher number please!")
        elif guess > random_number:
            print("🔽 Lower number please!")
        else:
            print(f"\n🎉 You guessed it in {guesses} attempt(s)! Well done!")
    except ValueError:
        print("❌ Please enter a valid integer.")
