import os
import json
from datetime import datetime

class Contact:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        contact = Contact(
            data["name"],
            data["phone"],
            data.get("email")
        )
        contact.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return contact
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email if self.email else 'N/A'}\n"
                f"Created: {self.created_at}")

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
    
    def add_contact(self, contact):
        if not self._validate_contact(contact):
            return False
        self.contacts.append(contact)
        return True
    
    def _validate_contact(self, contact):
        if not contact.name:
            print("Error: Name is required")
            return False
            
        if not validate_phone(contact.phone):
            print("Error: Phone must be exactly 10 digits")
            return False
            
        if any(c.phone == contact.phone for c in self.contacts):
            print("Error: Phone number already exists")
            return False
        
        if contact.email and not validate_email(contact.email):
            print("Error: Invalid email format")
            return False
            
        return True
    
    def view_contacts(self):
        return sorted(self.contacts, key=lambda x: x.name.lower())
    
    def search_contacts(self, keyword):
        keyword = keyword.lower()
        return [
            c for c in self.contacts
            if (keyword in c.name.lower() or 
                keyword in c.phone or 
                keyword in (c.email.lower() if c.email else ''))
        ]
    
    def delete_contact(self, phone):
        initial_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.phone != phone]
        return len(self.contacts) < initial_count
    
    def edit_contact(self, phone, **kwargs):
        for contact in self.contacts:
            if contact.phone == phone:
                for key, value in kwargs.items():
                    if value is not None:
                        setattr(contact, key, value)
                return True
        return False
    
    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving contacts: {e}")
            return False
    
    def load_from_file(self):
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    json.dump([], f)
                self.contacts = []
                return True
            
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(c) for c in data]
            return True
        except json.JSONDecodeError:
            print("Error: Invalid data in contacts file")
            return False
        except Exception as e:
            print(f"Error loading contacts: {e}")
            return False

def display_menu():
    print("\n=== Contact Book Manager ===")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Save and Exit")

def validate_phone(phone):
    """Validate that phone is exactly 10 digits and contains only numbers"""
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    """Basic email validation"""
    if not email:  # Empty is allowed (optional field)
        return True
    return '@' in email and '.' in email.split('@')[-1]

def get_contact_input():
    while True:
        name = input("Enter name: ").strip()
        if not name:
            print("Error: Name cannot be empty")
            continue
            
        phone = input("Enter phone (10 digits): ").strip()
        if not validate_phone(phone):
            print("Error: Phone must be exactly 10 digits (numbers only)")
            continue
            
        email = input("Enter email (optional): ").strip() or None
        if email and not validate_email(email):
            print("Error: Please enter a valid email (e.g., user@example.com)")
            continue
            
        return name, phone, email

def get_contact_to_edit(book):
    """Helper function to select a contact to edit"""
    contacts = book.view_contacts()
    if not contacts:
        print("\n📭 No contacts found")
        return None
        
    print("\n📇 Contact List:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c.name} ({c.phone})")
    
    try:
        choice = int(input("\nEnter contact number to edit: ")) - 1
        if 0 <= choice < len(contacts):
            return contacts[choice]
        print("Invalid contact number")
    except ValueError:
        print("Please enter a valid number")
    return None

def main():
    book = ContactBook()
    if not book.load_from_file():
        print("Starting with empty contact book")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            print("\nAdd New Contact")
            name, phone, email = get_contact_input()
            contact = Contact(name, phone, email)
            if book.add_contact(contact):
                print("✅ Contact added successfully!")
        
        elif choice == "2":
            contacts = book.view_contacts()
            if not contacts:
                print("\n📭 No contacts found")
            else:
                print("\n📇 Contact List:")
                for i, c in enumerate(contacts, 1):
                    print(f"\nContact #{i}")
                    print(f"Name: {c.name}")
                    print(f"Phone: {c.phone}")
                    print(f"Email: {c.email or 'N/A'}")
                    print("-" * 40)
        
        elif choice == "3":
            keyword = input("\nEnter search term: ").strip()
            results = book.search_contacts(keyword)
            if results:
                print(f"\n🔍 Found {len(results)} matching contacts:")
                for i, c in enumerate(results, 1):
                    print(f"\nContact #{i}")
                    print(c)
            else:
                print("\n❌ No matching contacts found")
        
        elif choice == "4":
            contact = get_contact_to_edit(book)
            if not contact:
                continue
                
            print("\nCurrent contact details:")
            print(contact)
            
            print("\nEnter new values (leave blank to keep current):")
            while True:
                name = input(f"Name [{contact.name}]: ").strip()
                name = name if name else contact.name
                
                phone = input(f"Phone [{contact.phone}]: ").strip()
                if not phone:
                    phone = contact.phone
                    break
                if validate_phone(phone):
                    break
                print("Error: Phone must be exactly 10 digits")
            
            while True:
                email = input(f"Email [{contact.email if contact.email else 'N/A'}]: ").strip()
                if not email:
                    email = contact.email
                    break
                if validate_email(email):
                    break
                print("Error: Please enter a valid email (e.g., user@example.com)")
            
            if book.edit_contact(contact.phone, name=name, phone=phone, email=email):
                print("✅ Contact updated successfully!")
        
        elif choice == "5":
            phone = input("\nEnter phone number of contact to delete: ").strip()
            if book.delete_contact(phone):
                print("✅ Contact deleted successfully!")
            else:
                print("❌ Contact not found")
        
        elif choice == "6":
            if book.save_to_file():
                print("💾 Contacts saved successfully!")
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
