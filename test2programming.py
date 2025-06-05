#menuLeya
def display_menu():
    print("\nWELCOME TO GRANN'S PHONE DIRECTORY")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Sort the record alphabetically")
    print("5. Delete a record")
    print("6. Quit")

#addLeya
def add_record(phone_directory):
    name = input("Enter name: ")
    phone = input("Enter a 10-digit phone number: ")
    if len(phone) == 10 and phone.isdigit():
        phone_directory[name] = phone
        print("Record added")
    else:
        print("Invalid phone number. Please enter a 10-digit number.")

#searchLeya
def search_record(phone_directory):
    name = input("Enter name to search: ")
    print(f"{name}: {phone_directory.get(name, 'Record not found.')}")

#updateLeya
def update_record(phone_directory):
    name = input("Enter name to update: ")
    if name in phone_directory:
        new_phone = input("Enter new 10-digit phone number: ")
        if len(new_phone) == 10 and new_phone.isdigit():
            phone_directory[name] = new_phone
            print("Record updated")
        else:
            print("Invalid phone number. Please enter a 10-digit number.")
    else:
        print("Record not found.")

#sorted alphabeticallyLeya
def sort_records(phone_directory):
    if phone_directory:
        print("\nSorted Records:")
        for name, phone in sorted(phone_directory.items()):
            print(f"{name} - {phone}")
    else:
        print("Phone directory is empty.")

#deleteLeya
def delete_record(phone_directory):
    name = input("Enter name to delete: ")
    if phone_directory.pop(name, None):
        print("Record deleted")
    else:
        print("Record not found.")

def main():
    phone_directory = {} 
    while True:
        display_menu() 
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_record(phone_directory)
        elif choice == "2":
            search_record(phone_directory)
        elif choice == "3":
            update_record(phone_directory)
        elif choice == "4":
            sort_records(phone_directory)
        elif choice == "5":
            delete_record(phone_directory)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break  
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
