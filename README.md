# Contact Manager

This is a simple command-line Contact Manager written in Python. It allows you to store, view, edit, and delete contact information (name, email, and phone number). Contacts are saved in a `contacts.json` file for persistent storage.

## Features
- Add new contacts
- View all contacts
- Edit existing contacts
- Delete contacts
- Persistent storage using JSON
- User-friendly menu interface
- Error and invalid input messages are highlighted for visibility

## How to Use
1. **Run the program:**
   ```
   python contact_manager.py
   ```
2. **Follow the on-screen menu:**
   - Add, view, edit, or delete contacts by choosing the corresponding option.
   - Enter the required information as prompted.
   - Contacts are automatically saved to `contacts.json` in the same directory.

## Requirements
- Python 3.x

## Notes
- The program uses ANSI color codes for error and success messages. If your terminal does not support colors, messages will still be visible as plain text.
- The contact list is stored in the same directory as the script.

## Example

```
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 2
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bob, Email: bob@example.com, Phone: 9876543210
3. Name: Charlie, Email: charlie@example.com, Phone: 5551234567
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 1
Enter name: David
Enter email: david@example.com
Enter phone: 1112223333
Contact added.
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 2
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bob, Email: bob@example.com, Phone: 9876543210
3. Name: Charlie, Email: charlie@example.com, Phone: 5551234567
4. Name: David, Email: david@example.com, Phone: 1112223333
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 3
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bob, Email: bob@example.com, Phone: 9876543210
3. Name: Charlie, Email: charlie@example.com, Phone: 5551234567
4. Name: David, Email: david@example.com, Phone: 1112223333
Enter contact number to edit: 2
Enter new name (leave blank to keep current): Bobby
Enter new email (leave blank to keep current): 
Enter new phone (leave blank to keep current): 9998887777
Contact updated.
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 4
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bob, Email: bob@example.com, Phone: 9876543210
3. Name: Charlie, Email: charlie@example.com, Phone: 5551234567
4. Name: Bobby, Email: david@example.com, Phone: 9998887777
Enter contact number to delete: 4
Contact deleted.
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 2
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bobby, Email: bob@example.com, Phone: 9998887777
3. Name: David, Email: david@example.com, Phone: 1112223333
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 7
Invalid choice. Please try again.
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option: 4
Contacts list:
1. Name: Alice, Email: alice@example.com, Phone: 1234567890
2. Name: Bobby, Email: bob@example.com, Phone: 9998887777
3. Name: David, Email: david@example.com, Phone: 1112223333
Enter contact number to delete: 7
Invalid contact index.
==============================
      Contact Manager
==============================
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Choose an option:5
Goodbye!
```


