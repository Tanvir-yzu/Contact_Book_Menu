from contact_manager import ContactManager

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

def main():
    manager = ContactManager()
    manager.load_contacts()  # Load contacts from the file at the start
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.remove_contact()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
