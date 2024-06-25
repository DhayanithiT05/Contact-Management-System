import json
import os

CONTACTS_FILES = 'contacts.json'

def load_cont():
    if os.path.exists(CONTACTS_FILES):
        with open(CONTACTS_FILES, 'r') as file:
            return json.load(file)
    return {}

def save_cont(contacts):
    with open(CONTACTS_FILES, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_cont(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone num: ")
    email = input("Enter email id: ")
    contacts[name] = {'phone': phone, 'email': email}
    save_cont(contacts)
    print(f"Contacts for {name} added.")
    
def view_cont(contacts):
    if not contacts:
        print("No contacts found...")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
            
def edit_cont(contacts):
    name = input("Enter the name of the contacts to edits: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter email id (current: {contacts[name]['email']}): ")
        contacts[name] = {'phone': phone, 'email': email}
        save_cont(contacts)
        print(f"Contacts for {name} updated...")
    else:
        print("Contact not found...")
        
def delete_cont(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_cont(contacts)
        print(f"Contacts for {name} deleted...")
    else:
        print("Contact not found...")
        
def main():
    contacts = load_cont()
    while True:
        print("\nContacts Management System")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_cont(contacts)
        elif choice == '2':
            view_cont(contacts)
        elif choice == '3':
            edit_cont(contacts)
        elif choice == '4':
            delete_cont(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again...")
            
if __name__ == "__main__":
    main()