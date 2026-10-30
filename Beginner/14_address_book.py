import json
import os
import re

CONTACTS_FILE = "contacts.json"

# Matches names that already end in a numbered suffix, e.g. "Rani (2)".
NUMBERED_NAME = re.compile(r"^(.*?)\s*\((\d+)\)$")


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def next_available_name(contacts, name):
    """Return the first free numbered name, e.g. 'Rani (2)', 'Rani (3)', ..."""
    base = name
    index = 2

    match = NUMBERED_NAME.match(name)
    if match:
        base = match.group(1)
        index = max(2, int(match.group(2)) + 1)

    while f"{base} ({index})" in contacts:
        index += 1
    return f"{base} ({index})"


def resolve_name(contacts, name):
    """Handle duplicate names without silently overwriting a contact.

    Returns the name to save the new contact under, or None if the user
    cancels. Existing contacts are only replaced after explicit confirmation.
    """
    if name not in contacts:
        return name

    existing = contacts[name]
    print(f"A contact named '{name}' already exists.")
    print(f"  Phone: {existing['phone']}, Email: {existing['email']}")
    suggested = next_available_name(contacts, name)

    while True:
        print("What would you like to do?")
        print("1. Overwrite the existing contact")
        print(f"2. Keep both (save the new contact as '{suggested}')")
        print("3. Cancel")
        choice = input("Enter your choice: ")

        if choice == "1":
            return name
        elif choice == "2":
            return suggested
        elif choice == "3":
            return None
        else:
            print("Invalid choice. Please try again.")


def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    name = resolve_name(contacts, name)
    if name is None:
        print("Contact not added.")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
