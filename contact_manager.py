import json
import os

# List to store contact dictionaries in memory
contacts = []
# File name for persistent storage
CONTACTS_FILE = 'contacts.json'

# Load contacts from the JSON file if it exists
def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            contacts = json.load(f)
    else:
        contacts = []

# Save the current contacts list to the JSON file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

# Add a new contact to the list and save
def create_contact(name, email, phone):
    contacts.append({'name': name, 'email': email, 'phone': phone})
    save_contacts()
    print("\033[92mContact added.\033[0m")  # Green text for success

# Display all contacts in a formatted list
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\033[92mContacts list:\033[0m")  # Green text for success
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

# Edit an existing contact by index and save
# Only updates fields that are provided (not None)
def edit_contact(index, name=None, email=None, phone=None):
    if 0 <= index < len(contacts):
        if name:
            contacts[index]['name'] = name
        if email:
            contacts[index]['email'] = email
        if phone:
            contacts[index]['phone'] = phone
        save_contacts()
        print("\033[92mContact updated.\033[0m")  # Green text for success
    else:
        print("\033[91mInvalid contact index.\033[0m")  # Red text for error

# Delete a contact by index and save
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts()
        print("\033[92mContact deleted.\033[0m")  # Green text for success
    else:
        print("\033[91mInvalid contact index.\033[0m")  # Red text for error

# Main menu loop for user interaction
def menu():
    while True:
        print("=" * 30)
        print("      Contact Manager      ")
        print("=" * 30)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            # Prompt user for new contact details
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            create_contact(name, email, phone)
        elif choice == '2':
            # Show all contacts
            view_contacts()
        elif choice == '3':
            # Edit a contact
            view_contacts()
            try:
                idx = int(input("Enter contact number to edit: ")) - 1
                name = input("Enter new name (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                phone = input("Enter new phone (leave blank to keep current): ")
                edit_contact(idx, name or None, email or None, phone or None)
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number.\033[0m")
        elif choice == '4':
            # Delete a contact
            view_contacts()
            try:
                idx = int(input("Enter contact number to delete: ")) - 1
                delete_contact(idx)
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number.\033[0m")
        elif choice == '5':
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Highlight invalid menu choices
            print("\033[93mInvalid choice. Please try again.\033[0m")  # Yellow text for invalid choice

# Run the program: load contacts and start the menu if run as main script
if __name__ == "__main__":
    load_contacts()
    menu()

