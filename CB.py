# Contact Book Program
contact_book = {}

# Function to add a new contact
def add_contact(name, phone, email):
    contact_book[name] = {'Phone': phone, 'Email': email}
    print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contact_book:
        print("\nAll Contacts:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("\nNo contacts found!")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"\nContact found: Name: {name}, Phone: {contact_book[name]['Phone']}, Email: {contact_book[name]['Email']}")
    else:
        print(f"\nContact with the name '{name}' not found!")

# Function to update a contact
def update_contact(name):
    if name in contact_book:
        new_phone = input(f"Enter new phone number for {name}: ")
        new_email = input(f"Enter new email for {name}: ")
        contact_book[name] = {'Phone': new_phone, 'Email': new_email}
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"Contact with the name '{name}' not found!")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"Contact with the name '{name}' not found!")

# Main program loop
def contact_book_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a valid number.")

# Run the contact book
contact_book_menu()
