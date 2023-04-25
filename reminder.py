import datetime
from birthdays import birthdays_list
from events import events_list
from telegram_bot import *

def check_birthday(when):
    if when == "Today":
        whan_date = datetime.date.today().strftime('%d/%m')
        complete_when_date = datetime.date.today().strftime('%d/%m/%Y')
    elif when == "Tomorrow":
        whan_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m')
        complete_when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    name_list=[]
    count_list=[]
    for name, date in birthdays_list.items():
        if date[:5] == whan_date:
            count=str(int(datetime.date.today().strftime('%Y'))-int(date[6:]))
            print(f"{when} is {name}'s birthday ({count})!")
            name_list.append(name)
            count_list.append(count)
    if len(name_list) == 0:
        return()
    else:
        send_telegram_msg(when, complete_when_date, name_list, count_list)

def check_events():
    print("events")
    today = datetime.date.today().strftime('%d/%m')
    complete_today = datetime.date.today().strftime('%d/%m/%Y')
    event_list=[]
    for name, date in events_list.items():
        if date[:5] == today:
            print(f"Reminder for today: {name}!")
            event_list.append(name)
    string_event_list = "\n".join(event_list)
    if len(string_event_list) == 0:
        return
    else:
        send_telegram_msg(complete_today, string_event_list)   


### PROGRAM ###
check_birthday("Today")
check_birthday("Tomorrow")
check_events()
