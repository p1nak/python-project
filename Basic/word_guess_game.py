import random
import os

class WordGuessGame:
    def __init__(self):
        self.words = {
            "python": "A popular programming language 🐍",
            "elephant": "The largest land animal 🐘",
            "guitar": "A string instrument 🎸",
            "pyramid": "Famous structure in Egypt 🏜️",
            "astronaut": "Travels to space 🚀"
        }
        self.max_attempts = 6
        self.chosen_word = random.choice(list(self.words.keys()))
        self.hint = self.words[self.chosen_word]
        self.guessed_letters = []
        self.attempts_left = self.max_attempts
        self.player_name = ""
        self.score_file = "scores.txt"

    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.chosen_word)

    def save_score(self, score):
        with open(self.score_file, "a") as f:
            f.write(f"{self.player_name}: {score}\n")

    def show_high_scores(self):
        if not os.path.exists(self.score_file):
            print("📄 No scores yet. Be the first one!")
            return

        print("\n🏆 High Scores:")
        with open(self.score_file, "r") as f:
            scores = []
            for line in f:
                name, score = line.strip().split(":")
                scores.append((name, int(score)))

        # Sort scores by value in descending order
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, (name, score) in enumerate(scores[:5], 1):
            print(f"{i}. {name} - {score}")

    def play(self):
        self.reset_game()  
        
        print(f"\n🔤 Welcome {self.player_name} to the Word Guessing Game!")
        print("💡 Hint:", self.hint)

        while self.attempts_left > 0:
            print("\nWord:", self.display_word())
            print(f"❤️ Attempts left: {self.attempts_left}")
            guess = input("🔠 Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Enter a single alphabetical character!")
                continue

            if guess in self.guessed_letters:
                print("🔁 You already guessed that letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.chosen_word:
                print("✅ Good guess!")
            else:
                self.attempts_left -= 1
                print("❌ Wrong guess.")

            if all(letter in self.guessed_letters for letter in self.chosen_word):
                print("\n🎉 Congratulations! You guessed the word:", self.chosen_word)
                score = self.attempts_left * 10
                print(f"🏅 Your Score: {score}")
                self.save_score(score)
                self.show_high_scores()
                break
        else:
            print("\n😢 Out of attempts! The word was:", self.chosen_word)
            print("🏅 Your Score: 0")
            self.save_score(0)
            self.show_high_scores()


    def start(self):
        self.player_name = input("👤 Enter your name: ").strip().title()
        while True:
            self.play()
            again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
            if again not in ["yes", "y"]:
                print("👋 Thanks for playing, goodbye!")

    def reset_game(self):
        self.chosen_word = random.choice(list(self.words.keys()))
        self.hint = self.words[self.chosen_word]
        self.guessed_letters = []
        self.attempts_left = self.max_attempts
        
# Run the game
if __name__ == "__main__":
    game = WordGuessGame()
    game.start()
