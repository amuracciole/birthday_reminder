import datetime
import os
import time
from birthdays import birthdays_list
from events import events_list

def main_menu():
    print("1 - Add event")
    print("2 - Delete event")
    print("3 - See event")
    print("0 - EXIT\n")
    
def add_event_menu():
    print("1 - Add birthday")
    print("2 - Add other event")
    print("0 - EXIT\n")
    
def delete_event_menu():
    print("1 - Delete birthday")
    print("2 - Delete other event")
    print("0 - EXIT\n")

def see_event_menu():
    print("1 - See birthdays")
    print("2 - See other events")
    print("0 - EXIT\n")
    
### PROGRAM ###
while (True):
    main_menu()
    main_option = input("OPTION: ")
    if (main_option == "1"):
        os.system('clear')
        add_event_menu()
        option = input("OPTION: ")
        if option == "1":
            name = input("Name of the person: ")
            date = input("Enter the birthday in the format DDMMYYYY: ")
            try:
                date = datetime.datetime.strptime(date, "%d%m%Y")
                birthdays_list[name] = date.strftime("%d/%m/%Y")
                with open('birthdays.py', 'w') as f:
                    f.write('birthdays_list = ' + str(birthdays_list))
                print("Added successfully!")
            except ValueError:
                print("Invalid date format. Try again.")
                break
            time.sleep(1)
            os.system('clear')
        elif option == "2":
            event_name = input("Name of the event: ")
            event_date = input("Enter the date in the format DDMM: ")
            try:
                event_date = datetime.datetime.strptime(event_date, "%d%m")
                events_list[event_name] = event_date.strftime("%d/%m")
                with open('events.py', 'w') as f:
                    f.write('events_list = ' + str(events_list))
                print("Added successfully!")
            except ValueError:
                print("Invalid date format. Try again.")
                break
            time.sleep(1)
            os.system('clear')
        elif option =="0":
            os.system('clear')
            break  
    
    elif main_option == "2":
        os.system('clear')
        delete_event_menu()
        option = input("OPTION: ")
        if option == "1":
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
        elif option == "2":
            os.system('clear')
            print("Select the number of the entry to delete:\n")
            with open('events.py', 'r') as f:
                exec(f.read()) 
            for i, event_name in enumerate(events_list):
                print(f"{i + 1}. {event_name} - {events_list[event_name]}")
            selection = input("Selection: ")
            try:
                index = int(selection) - 1
                event_to_delete = list(events_list.keys())[index]
                events_list.pop(event_to_delete)
                with open('events.py', 'w') as f:
                    f.write('events_list = ' + str(events_list))
                print(f"\nDeleted {event_to_delete}")
            except (ValueError, IndexError):
                print("\nInvalid selection. Try again.")
            os.system('clear')
        elif option =="0":
            os.system('clear')
            break  
    
    elif main_option == "3":
        os.system('clear')
        see_event_menu()
        option = input("OPTION: ")
        if option == "1":
            os.system('clear')
            with open('birthdays.py', 'r') as f:
                exec(f.read())
            for name, date in birthdays_list.items():
                print(f"{name} - {date}")
            input("\nPress enter to continue")
            os.system('clear')
        elif option =="2":
            os.system('clear')
            with open('events.py', 'r') as f:
                exec(f.read())
            for event_name, event_date in events_list.items():
                print(f"{event_name} - {event_date}")
            input("\nPress enter to continue")
            os.system('clear')
        elif option =="0":
            os.system('clear')
            break   
    
    elif main_option == "0":
        os.system('clear')
        break