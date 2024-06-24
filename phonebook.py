from numpy import number


contact_list= {}
   
def list_all_contact(contact_list):
    if not contact_list:
        print("contact_list is empty")
    else:
        for name, details in contact_list.items():
            print(f"Name: {name}, number: {details["number"]}, email: {details["email"]}")

def add_contact(contact_list):
    name = input("enter a name of a contact: ")
    number = input("enter a number of a contact: ")
    email = input("enter an email id of a contact: ")
    contact_list[name] = {'number': number, 'email': email}
    print(f"Contact {name} added successfully.")


def update_contact(contact_list):
    list_all_contact(contact_list)
    name = input("enter a name of a contact  you want to update: ")

    if name in contact_list:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact_list[name] = {'number': number, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"contact {name} not found.")


def delete_contact():
    list_all_contact(contact_list)
    name = input("enter a name of a contact  you want to delete: ")

    if name in contact_list:
        del contact_list[name]
        print(f"contact {name} delete successfully")
    else:
        print(f"contact {name} not found.")


while True:
    print("\n contact list | choose an option")
    print("1. list all contact")
    print("2. add a contact")
    print("3. update a contactr")
    print("4. delete a contact")
    print("5. exit the app")
    choice = input("enter your choice: ")
    print(contact_list)
    match str(choice):
            case "1":
                list_all_contact(contact_list)
            case "2":
                add_contact(contact_list)
            case "3":
                update_contact(contact_list)
            case "4":
                delete_contact(contact_list)                
            case "5":
                ("Exiting the app...")
                break
            case _:
                print("invalid input")