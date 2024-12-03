import csv
from validators import validate_name, validate_phone_number, validate_email
from file_manager import load_from_file, save_to_file

class ContactManager:
    def __init__(self):
        self.contacts = []

    def load_contacts(self):
        self.contacts = load_from_file()

    def save_contacts(self):
        save_to_file(self.contacts)

    def add_contact(self):
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        address = input("Enter Address: ").strip()

        if not validate_name(name):
            print("Error: Name must be a valid string.")
            return
        if not validate_email(email):
            print("Error: Invalid email format.")
            return
        if not validate_phone_number(phone, self.contacts):
            print("Error: Phone number must be unique and numeric.")
            return

        contact = {"name": name, "email": email, "phone": phone, "address": address}
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\n--- Contact List ---")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

    def search_contact(self):
        term = input("Enter name, email, or phone to search: ").strip().lower()
        results = [contact for contact in self.contacts if term in contact["name"].lower() or term in contact["email"].lower() or term in contact["phone"]]
        if not results:
            print("No contacts found.")
            return
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")

    def remove_contact(self):
        if not self.contacts:
            print("No contacts available to remove.")
            return

        self.view_contacts()
        while True:
            try:
                index = input("Enter the Sl number to remove (or 'q' to quit): ").strip()
                if index.lower() == 'q':
                    print("Contact removal cancelled.")
                    return
                index = int(index)
                if index <= 0 or index > len(self.contacts):
                    print("Error: Invalid contact number. Please try again.")
                    continue
                removed_contact = self.contacts.pop(index - 1)
                self.save_contacts()
                print(f"Contact '{removed_contact['name']}' removed successfully!")
                break
            except ValueError:
                print("Error: Please enter a valid number.")
