import os
from datetime import datetime

NOTEPAD = "notepad.txt"

def load_notes():
    if os.path.exists(NOTEPAD):
        with open(NOTEPAD , "r") as note:
            return note.read().splitlines()

def save_notes(notes):
    with open(NOTEPAD , "w") as note:
        note.write("\n".join(notes))

def add_note(notes):
    new_note = input("📝Write notes : ").strip()

    if new_note:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_note = f"{new_note} | {timestamp}"
        notes.append(formatted_note)
        print("✅ Note added with timestamp.")
    else:
        print("Note cannot be empty!")

def show_notes(notes):
    if not notes:
        print("no notes yet!")
    
    else:
        print("\nYour notes : ")
        for i , note in enumerate(notes , 1):
            if "|" in note:
                content, time = note.rsplit("|", 1)
                print(f"{i}. {content.strip()} 🕒 {time.strip()}")
            else:
                print(f"{i}. {note}")

def delete_note(notes):
    show_notes(notes)
    if not notes:
        return
    
    try:
        index = int(input("Enter note number to delete : "))

        if 1<= index <= len(notes):
            deleted = notes.pop(index-1)
            print(f"deleted : {deleted}")
        else:
            print("❌invalid number")
    except ValueError:
        print("❌please enter valid nimber")

def main():

    notes = load_notes()

    while True:
        print("\nOption")
        print("1. Add note")
        print("2. view note")
        print("3. save note")
        print("4. delete note")
        print("5. load note")
        print("6. Exit")

        choice = input("👉 Choose an option (1-6): ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            save_notes(notes)
            print("💾 Notes saved!")
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            notes = load_notes()
            print("📂 Notes reloaded!")
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
