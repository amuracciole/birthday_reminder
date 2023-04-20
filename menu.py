import datetime
import os
import time
from birthdays import birthdays_list

def menu():
    print("1 - Add birthday")
    print("2 - Delete birthday")
    print("3 - See birthday list")
    print("0 - EXIT\n")
    
### PROGRAM ###
while (True):
    menu()
    option = input("OPTION: ")
    if option == "1":
        name = input("Name of the person: ")
        date = input("Enter the birthday in the format DD-MM-YYYY: ")
        try:
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            birthdays_list[name] = date.strftime("%d-%m-%Y")
            with open('birthdays.py', 'w') as f:
                f.write('birthdays_list = ' + str(birthdays_list))
            print("Added successfully!")
        except ValueError:
            print("Invalid date format. Try again.")
            break
        time.sleep(1)
        os.system('clear')
    elif option == "2":
        os.system('clear')
        print("Select the number of the entry to delete:\n")
        with open('birthdays.py', 'r') as f:
            exec(f.read()) 
        for i, name in enumerate(birthdays_list):
            print(f"{i + 1}. {name} - {birthdays_list[name]}")
        selection = input("Selection: ")
        try:
            index = int(selection) - 1
            name_to_delete = list(birthdays_list.keys())[index]
            birthdays_list.pop(name_to_delete)
            with open('birthdays.py', 'w') as f:
                f.write('birthdays_list = ' + str(birthdays_list))
            print(f"\nDeleted {name_to_delete}")
        except (ValueError, IndexError):
            print("\nInvalid selection. Try again.")
        os.system('clear')
    elif option == "3":
        os.system('clear')
        with open('birthdays.py', 'r') as f:
            exec(f.read())
        for name, date in birthdays_list.items():
            print(f"{name} - {date}")
        input("\nPress enter to continue")
        os.system('clear')
    elif option == "0":
        os.system('clear')
        break