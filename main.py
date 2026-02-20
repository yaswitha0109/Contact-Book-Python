import os

FILE_NAME = "contacts.txt"


# ----------- Create File if Not Exists -----------
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass


# ----------- Add Contact -----------
def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        with open(FILE_NAME, "a") as file:
            file.write(name + "," + phone + "\n")

        print("Contact added successfully!\n")

    except PermissionError:
        print("Permission Denied! Close contacts.txt if it is open.\n")


# ----------- View Contacts -----------
def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

            if len(contacts) == 0:
                print("No contacts found.\n")
                return

            print("\nContact List:")
            print("-------------------------")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print("Name:", name, "| Phone:", phone)
            print()

    except FileNotFoundError:
        print("File not found.\n")


# ----------- Search Contact -----------
def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")

                if name.lower() == search_name.lower():
                    print("Contact Found!")
                    print("Name:", name)
                    print("Phone:", phone)
                    print()
                    found = True
                    break

        if not found:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


# ----------- Main Menu -----------
def main():
    create_file()

    while True:
        print("===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()