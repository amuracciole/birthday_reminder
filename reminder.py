# -*- coding: utf-8 -*-

import datetime
from birthdays import birthdays_list
from events import events_list
from telegram_bot import *

def check_birthday(when):
    if when == "Today":
        when_date = datetime.date.today().strftime('%d/%m')
        complete_when_date = datetime.date.today().strftime('%d/%m/%Y')
    elif when == "Tomorrow":
        when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m')
        complete_when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    name_list=[]
    count_list=[]
    for name, date in birthdays_list.items():
        if date[:5] == when_date:
            count=str(int(datetime.date.today().strftime('%Y'))-int(date[6:]))
            print(f"{when} is {name}'s birthday ({count})!")
            name_list.append(name)
            count_list.append(count)
    if len(name_list) == 0:
        return()
    else:
        send_telegram_msg(when, complete_when_date, name_list, count_list)

def check_event(when):
    if when == "Today":
        when_date = datetime.date.today().strftime('%d/%m')
        complete_when_date = datetime.date.today().strftime('%d/%m/%Y')
    elif when == "Tomorrow":
        when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m')
        complete_when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    event_list=[]
    for event, date in events_list.items():
        if date[:5] == when_date:
            print(f"Reminder for today: {event}!")
            event_list.append(event)
    if len(event_list) == 0:
        return()
    else:
        send_telegram_msg(when, complete_when_date, event_list, "null")  

### PROGRAM ###
check_birthday("Today")
check_birthday("Tomorrow")
check_event("Today")
check_event("Tomorrow")
