#contact book
contact={"Police":100,"Ambulance":911,"Fire":101}

def addContact():
    name=input("Enter contact name:")
    number= int(input("Enter number:"))
    contact[name]=number
    print("Contact added successfully")

def deleteContact():
    name=input("Enter the contact name to delete:")
    if name in contact:
        del contact[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def updateContact():
    name=input("Enter the contact name to update:")
    if name in contact:
        number=int(input("Enter number:"))
        contact[name]=number
        print("Contact updates successfully.")
    else:
        print("Contact not found.")


def listContact():
    for k,v in contact.items():
        print(k,v)

listContact()
addContact()
listContact()
updateContact()
listContact()