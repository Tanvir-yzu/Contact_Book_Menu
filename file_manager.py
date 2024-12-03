import csv

FILE_NAME = "contacts.csv"

def load_from_file():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def save_to_file(contacts):
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["name", "email", "phone", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
