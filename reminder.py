import datetime
from birthdays import birthdays_list
from events import events_list
from telegram_bot import *

def check_birthday():
    today = datetime.date.today().strftime('%d-%m-%Y')
    name_list=[]
    for name, date in birthdays_list.items():
        if date == today:
            print(f"Today is {name}'s birthday!")
            name_list.append(name)
    string_name_list = "\n".join(name_list)
    #print(string_name_list,len(string_name_list))
    if len(string_name_list) == 0:
        exit()
    else:
        send_telegram_msg(today, string_name_list)

def check_events():
    today = datetime.date.today().strftime('%d-%m-%Y')
    event_list=[]
    for name, date in events_list.items():
        if date == today:
            print(f"Reminder for today: {name}!")
            event_list.append(name)
    string_event_list = "\n".join(event_list)
    #print(string_name_list,len(string_name_list))
    if len(string_event_list) == 0:
        exit()
    else:
        send_telegram_msg(today, string_event_list)   

### PROGRAM ###
check_birthday()
check_events()