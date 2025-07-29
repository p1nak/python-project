import json
import os

def load_questions(filename="quiz_questions.json"):
    if not os.path.exists(filename):
        return []
    
    with open(filename, "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    right_answers = 0
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question["options"], 1):
            print(f"{j}. {option}")
        
        while True:
            try:
                user_input = int(input("Your answer (1-4): ")) - 1
                if 0 <= user_input < len(question["options"]):
                    break
                print("Invalid choice. Enter a number between 1-4!")
            except ValueError:
                print("Please enter a number!")
        
        if question["options"][user_input] == question["answer"]:
            print("\n✅ Correct!")
            score += 3
            right_answers += 1
        else:
            print(f"\n❌ Wrong! The correct answer was {question['answer']}")
            score -= 1
    
    return score, right_answers

def main():
    print("🌟 Welcome to the Python Quiz! 🌟")
    questions = load_questions()
    
    if not questions:
        print("Error: No questions found. Please check quiz_questions.json")
        return
    
    input("Press Enter to start the quiz...")
    total_questions = len(questions)
    score, right_answers = run_quiz(questions)  # Only call once

    print(f"\n🎉 Quiz Complete! 🎉")
    print(f"Your Right Answers: {right_answers}/{total_questions}")
    print(f"Your score: {score} (Max possible: {total_questions * 3})")
    print(f"Percentage: {(right_answers/total_questions)*100:.1f}%")

if __name__ == "__main__":
    main()
