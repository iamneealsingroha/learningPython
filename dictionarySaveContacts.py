contacts = {"Ravi Singroha":9717196269,
             "Pallavi Sharma": 9311064242,
             "Arjun Malhotra": 8451666687,
             "Ananya Iyer":5174843739,
             "Ishaan Mukherjee":6777865304,
             "Zoya Deshmukh": 3238405684,
             "Vihaan Reddy":6516333378}
print("Contacts :-")
for a in contacts:
    print(a, ":", contacts[a])
z = int(input("How many changes do you want to make in the contact list : "))
for i in range(z):
    b =input("Choose one option to do the list -  add contact, delete contact, show list, exit program :  ")
    if b == "add contact":
        d = input("Enter the name of the contact : ")
        e = int(input("Enter the number of the contact : "))
        contacts[d] = e
        print("Contact added successfully!")
    elif b == "delete contact":
        f = input("Enter the name of the contact you want to delete : ")
        del contacts[f]
        print("Contact deleted successfully!")
    elif b == "show list":
        print("Contacts :-")
        for a in contacts:
            print(a, ":", contacts[a])
    elif b == "exit program":
        print("Exiting the program...")
        break