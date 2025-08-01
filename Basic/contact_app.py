import os
import json

class contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email
        }
    
    @staticmethod
    def from_dict(data):
        return contact(data["name"], data["phone"], data["email"])

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact(self):
        return self.contacts

    def search_contact(self, name):
        return [c for c in self.contacts if name.lower() in c.name.lower()]

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]

    def save_contacts(self):
        with open(self.filename , "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f ,indent = 4)

    def load_contacts(self):
        if not os.path.exists(self.filename):
            # Auto-create an empty JSON file if it doesn't exist
            with open(self.filename, "w") as f:
                json.dump([], f)
            self.contacts = []
        else:
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(c) for c in data]
            except (FileNotFoundError, json.JSONDecodeError):
                self.contacts = []

def main():
    book = ContactBook()
    book.load_contacts()

    while True:
        print("\n=== Contact Book 📒 ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save and Exit")

        choice = input("👉 Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            book.add_contact(contact(name, phone, email))
            print("✅ Contact added!")
        
        elif choice == "2":
            if not book.contacts:
                print("📭 No contacts found.")
            else:
                print("\n📇 Contact List:")
                print(f"{'No.':<4} {'Name':<20} {'Phone':<15} {'Email'}")
                print("-" * 60)
                for i, c in enumerate(book.contacts, 1):
                    print(f"{i:<4} {c.name:<20} {c.phone:<15} {c.email}")
        
        elif choice == "3":
            keyword = input("🔍 Search by name: ").strip()
            results = book.search_contact(keyword)
            if results:
                print(f"\n🔍 Search Results:")
                print(f"{'No.':<4} {'Name':<20} {'Phone':<15} {'Email'}")
                print("-" * 60)
                for i, c in enumerate(results, 1):
                    print(f"{i:<4} {c.name:<20} {c.phone:<15} {c.email}")
            else:
                print("❌ No contact found.")
        
        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            book.delete_contact(name)
            print("🗑️ Contact deleted (if it existed).")
        
        elif choice == "5":
            book.save_contacts()
            print("💾 Saved! Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
