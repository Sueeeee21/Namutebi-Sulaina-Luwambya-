import re
import os

class ContactManager:

    def __init__(self):
        # I am using a list to store all contacts
        # Each contact is a tuple like (name, phone, email)
        self.contacts = []

    def add_contact(self, name, phone, email=""):
        if not re.match(r'^[0-9+\-]+$', phone):
            print("Error: Phone number can only have digits and hyphens (e.g. +256-701-123456)")
            return

        if email != "":
            if not re.search(r'@', email) or not re.search(r'\.', email):
                print("Error: Email must have an @ and a dot in it")
                return

        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                print("A contact with that name already exists!")
                return

        self.contacts.append((name, phone, email))
        print("Contact added successfully!")

    def view_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                print("-----------------------------")
                print("Name  :", contact[0])
                print("Phone :", contact[1])
                if contact[2] != "":
                    print("Email :", contact[2])
                else:
                    print("Email : (not provided)")
                print("-----------------------------")
                return
        print("Contact not found.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for i in range(len(self.contacts)):
            if self.contacts[i][0].lower() == name.lower():

                # get current values
                current_name = self.contacts[i][0]
                current_phone = self.contacts[i][1]
                current_email = self.contacts[i][2]

                # validate new phone if user wants to change it
                if new_phone != None:
                    if not re.match(r'^[0-9+\-]+$', new_phone):
                        print("Error: Phone number can only have digits and hyphens")
                        return
                    current_phone = new_phone

                # validate new email if user wants to change it
                if new_email != None:
                    if new_email != "":
                        if not re.search(r'@', new_email) or not re.search(r'\.', new_email):
                            print("Error: Email must have an @ and a dot in it")
                            return
                    current_email = new_email

                # save the updated contact
                self.contacts[i] = (current_name, current_phone, current_email)
                print("Contact updated!")
                return

        print("Contact not found.")

    def delete_contact(self, name):
        for i in range(len(self.contacts)):
            if self.contacts[i][0].lower() == name.lower():
                self.contacts.pop(i)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def search_contacts(self, keyword):
        keyword = keyword.lower()
        results = []

        for contact in self.contacts:
            # search by name, phone or email
            if keyword in contact[0].lower():
                results.append(contact)
            elif keyword in contact[1].lower():
                results.append(contact)
            elif keyword in contact[2].lower():
                results.append(contact)

        if len(results) == 0:
            print("No contacts matched your search.")
        else:
            print(f"\nFound {len(results)} result(s) for '{keyword}':")
            print("=" * 35)
            for contact in results:
                print("Name  :", contact[0])
                print("Phone :", contact[1])
                if contact[2] != "":
                    print("Email :", contact[2])
                else:
                    print("Email : (not provided)")
                print("-" * 35)

    def list_all_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts saved yet.")
            return

        print(f"\nAll Contacts ({len(self.contacts)} total):")
        print("=" * 35)
        for contact in self.contacts:
            print("Name  :", contact[0])
            print("Phone :", contact[1])
            if contact[2] != "":
                print("Email :", contact[2])
            else:
                print("Email : (not provided)")
            print("-" * 35)


def main():
    manager = ContactManager()

    while True:
        # clear the screen so the menu looks clean each time
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number (e.g. +256-701-123456): ")
            email = input("Enter email (press Enter to skip): ")
            manager.add_contact(name, phone, email)
            input("\nPress Enter to continue...")

        elif choice == "2":
            name = input("Enter name to view: ")
            manager.view_contact(name)
            input("\nPress Enter to continue...")

        elif choice == "3":
            name = input("Enter name of contact to update: ")
            print("Leave blank to keep the current value")
            new_phone = input("New phone number: ")
            new_email = input("New email: ")

            # only pass values that the user actually typed
            if new_phone == "" and new_email == "":
                print("Nothing to update.")
            elif new_phone == "":
                manager.update_contact(name, new_email=new_email)
            elif new_email == "":
                manager.update_contact(name, new_phone=new_phone)
            else:
                manager.update_contact(name, new_phone=new_phone, new_email=new_email)
            input("\nPress Enter to continue...")

        elif choice == "4":
            name = input("Enter name of contact to delete: ")
            manager.delete_contact(name)
            input("\nPress Enter to continue...")

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            manager.search_contacts(keyword)
            input("\nPress Enter to continue...")

        elif choice == "6":
            manager.list_all_contacts()
            input("\nPress Enter to continue...")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")
            input("\nPress Enter to continue...")


main()
