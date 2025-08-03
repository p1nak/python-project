import requests
import json
import random
import os
from html import unescape

# Available categories from Open Trivia DB
CATEGORIES = {
    9: "General Knowledge",
    10: "Entertainment: Books",
    11: "Entertainment: Film",
    12: "Entertainment: Music",
    13: "Entertainment: Musicals & Theatres",
    14: "Entertainment: Television",
    15: "Entertainment: Video Games",
    16: "Entertainment: Board Games",
    17: "Science & Nature",
    18: "Science: Computers",
    19: "Science: Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Entertainment: Comics",
    30: "Science: Gadgets",
    31: "Entertainment: Japanese Anime & Manga",
    32: "Entertainment: Cartoon & Animations"
}

DIFFICULTIES = ["easy", "medium", "hard"]

def fetch_questions(amount, category, difficulty):
    # Fetch questions from Open Trivia Database API
    base_url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "category": category,
        "difficulty": difficulty,
        "type": "multiple"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["response_code"] != 0:
            raise ValueError("API returned no results")
            
        return [format_question(q) for q in data["results"]]
    except Exception as e:
        print(f"⚠️ Error fetching questions: {e}")
        return []

def format_question(api_question):
    """Format API question to our quiz format"""
    question = {
        "question": unescape(api_question["question"]),
        "options": [unescape(ans) for ans in api_question["incorrect_answers"]] + [unescape(api_question["correct_answer"])],
        "answer": unescape(api_question["correct_answer"])
    }
    random.shuffle(question["options"])
    return question

def get_user_preferences():
    """Get quiz preferences from user"""
    print("\n⚙️ Quiz Customization")
    
    # Amount selection
    while True:
        try:
            amount = int(input("Number of questions (1-50): "))
            if 1 <= amount <= 50:
                break
            print("Please enter a number between 1-50")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Category selection
    print("\nAvailable Categories:")
    for id, name in CATEGORIES.items():
        print(f"{id}: {name}")
    
    while True:
        try:
            category = int(input("\nSelect category ID: "))
            if category in CATEGORIES:
                break
            print("Invalid category ID! Please choose from the list.")
        except ValueError:
            print("Please enter a number.")
    
    # Difficulty selection
    print("\nAvailable Difficulties:")
    for i, diff in enumerate(DIFFICULTIES, 1):
        print(f"{i}. {diff.capitalize()}")
    
    while True:
        try:
            choice = int(input("\nSelect difficulty (1-3): "))
            if 1 <= choice <= 3:
                difficulty = DIFFICULTIES[choice-1]
                break
            print("Please enter a number between 1-3")
        except ValueError:
            print("Invalid input!")
    
    return amount, category, difficulty

def run_quiz(questions):
    score = 0
    right_answers = 0
    max_possible_score = len(questions) * 3
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        
        for j, option in enumerate(question["options"], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                user_choice = int(input("Your answer (1-4): ")) - 1
                if 0 <= user_choice < len(question["options"]):
                    break
                print("Please enter a number between 1-4!")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        if question["options"][user_choice] == question["answer"]:
            print("✅ Correct! (+3 points)")
            score += 3
            right_answers += 1
        else:
            print(f"❌ Wrong! (-1 point) The correct answer was: {question['answer']}")
            score -= 1
    
    print(f"\n🎉 Quiz Complete! 🎉")
    print(f"Right Answers: {right_answers}/{len(questions)}")
    print(f"Total Score: {score} (Max Possible: {max_possible_score})")
    print(f"Percentage: {(score/max_possible_score)*100:.1f}%")

def main():
    print("🌟 Trivia Quiz Master 🌟")
    print("Customize your quiz experience!\n")
    
    amount, category, difficulty = get_user_preferences()
    
    print(f"\n🔮 Generating your quiz...")
    print(f"Questions: {amount} | Category: {CATEGORIES[category]} | Difficulty: {difficulty.capitalize()}")
    
    questions = fetch_questions(amount, category, difficulty)
    
    if not questions:
        print("Failed to load questions. Please try again later.")
        return
    
    input("\nPress Enter to start the quiz...")
    run_quiz(questions)

if __name__ == "__main__":
    main()
