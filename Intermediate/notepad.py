import os
import shutil
from datetime import datetime

NOTEPAD_FILE = "notepad.txt"

def load_notes():
 
    try:
        if os.path.exists(NOTEPAD_FILE):
            with open(NOTEPAD_FILE, "r", encoding="utf-8") as file:
                return file.read().splitlines()
        return []
    except Exception as e:
        print(f"❌ Error loading notes: {e}")
        return []

def save_notes(notes):
    
    try:
        # Create backup before saving
        if os.path.exists(NOTEPAD_FILE):
            backup_notes()
            
        with open(NOTEPAD_FILE, "w", encoding="utf-8") as file:
            file.write("\n".join(notes))
        return True
    except Exception as e:
        print(f"❌ Error saving notes: {e}")
        return False

def backup_notes():
  
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"notepad_backup_{timestamp}.txt"
        shutil.copy(NOTEPAD_FILE, backup_file)
        print(f"📂 Backup created: {backup_file}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def add_note(notes):
   
    print("\n📝 Enter your note (type 'END' on a new line to finish):")
    note_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        note_lines.append(line)
    
    if note_lines:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes.append(f"{'\n'.join(note_lines)} | {timestamp}")
        print("✅ Note added successfully!")
    else:
        print("⚠️ Empty note discarded")

def show_notes(notes, search_term=None):
  
    if not notes:
        print("\nNo notes yet! Add some notes first.")
        return
    
    filtered_notes = notes
    if search_term:
        filtered_notes = [n for n in notes if search_term.lower() in n.lower()]
        if not filtered_notes:
            print(f"\nNo notes found matching: '{search_term}'")
            return
    
    print("\n📋 Your Notes:")
    max_width = len(str(len(filtered_notes)))
    for i, note in enumerate(filtered_notes, 1):
        if "|" in note:
            content, time = note.rsplit("|", 1)
            content = content.strip()
            time = time.strip()
        else:
            content = note
            time = "No timestamp"
        
        # Print numbered note with indentation for multi-line notes
        lines = content.split('\n')
        print(f"{i:>{max_width}}. {lines[0]} 🕒 {time}")
        for line in lines[1:]:
            print(" " * (max_width + 2) + line)

def delete_note(notes):
    
    show_notes(notes)
    if not notes:
        return
    
    try:
        index = int(input("\nEnter note number to delete: "))
        if 1 <= index <= len(notes):
            print(f"\nNote to delete:\n{notes[index-1]}")
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == 'y':
                deleted = notes.pop(index-1)
                print(f"🗑️ Deleted note #{index}")
            else:
                print("Deletion cancelled")
        else:
            print("❌ Invalid note number")
    except ValueError:
        print("❌ Please enter a valid number")

def search_notes(notes):
    
    term = input("\n🔍 Enter search term: ").strip()
    show_notes(notes, search_term=term)

def clear_all_notes():
   
    confirm = input("⚠️ Delete ALL notes? This cannot be undone! (y/n): ").lower()
    if confirm == 'y':
        try:
            if os.path.exists(NOTEPAD_FILE):
                os.remove(NOTEPAD_FILE)
            print("🧹 All notes cleared!")
            return []
        except Exception as e:
            print(f"❌ Error clearing notes: {e}")
    else:
        print("Operation cancelled")
    return None

def main():
    notes = load_notes()
    
    while True:
        print("\n" + "="*30)
        print("📒 Enhanced Notepad".center(30))
        print("="*30)
        print("1. Add New Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Save Notes")
        print("5. Delete a Note")
        print("6. Clear All Notes")
        print("7. Exit")
        
        choice = input("\n👉 Choose an option (1-7): ").strip()
        
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            if save_notes(notes):
                print("💾 Notes saved successfully!")
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            result = clear_all_notes()
            if result is not None:  # Only update if user confirmed
                notes = result
        elif choice == "7":
            # Auto-save on exit
            if notes and input("Save before exiting? (y/n): ").lower() == 'y':
                save_notes(notes)
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
