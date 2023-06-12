# -*- coding: utf-8 -*-

import datetime
import os
import time
import json

def main_menu():
    print("1 - Add event")
    print("2 - Delete event")
    print("3 - See event")
    print("0 - EXIT\n")

def add_value(name, type, date, recurrency):
    with open('events.json', encoding='utf-8') as file:
        data = json.load(file)
    new_event = {
        "name": name,
        "type": type,
        "date": date,
        "recurrency": recurrency
    }
    data['events'].append(new_event)
    with open('events.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

### PROGRAM ###
while (True):
    os.system('clear')
    main_menu()
    main_option = input("OPTION: ")
    if (main_option == "1"):
        os.system('clear')
        type = "Event"
        name = input("Name of the birthday person / event: ")
        date = input("Enter the date in the format DDMMYYYY: ")
        type = input("Birthday (B) or Other (O): ")
        if (type == "B" or type == "b"):
            type = "Birthday"
        elif (type == "O" or type == "o"):
            type = "Event"
        recurrency = input("Recurrenty (Y/N): ")
        if (recurrency == "Y" or recurrency == "y"):
            recurrency = True
        elif (recurrency == "N" or recurrency == "n"):
            recurrency = False
        try:
            date = datetime.datetime.strptime(date, "%d%m%Y")
            date = date.strftime("%d/%m/%Y")
            add_value (name, type, date, recurrency)
            print("Added successfully!")
        except ValueError:
            print("Invalid date format. Try again.")
            break
        time.sleep(1)
        os.system('clear')
    
    elif main_option == "2":
        os.system('clear')
        print("Select the number of the entry to delete:\n")
        with open('events.json', encoding='utf-8') as file:
            data = json.load(file)
        for i, event in enumerate(data['events'], start=1):
            print(f"{i} - {json.dumps(event)}")
        selection = input("Selection: ")
        try:
            del data['events'][int(selection) - 1]
            with open('events.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            print("Entrada eliminada con éxito.")
        except (ValueError, IndexError):
            print("\nInvalid selection. Try again.")
        os.system('clear')
    
    elif main_option == "3":
        os.system('clear')
        with open('events.json') as file:
            data = json.load(file)
        for i, event in enumerate(data['events'], start=1):
            print(f"{i} - {json.dumps(event)}")
        input("\nPress enter to continue")
        os.system('clear')  
    
    elif main_option == "0":
        os.system('clear')
        break