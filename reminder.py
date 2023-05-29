# -*- coding: utf-8 -*-

import datetime
from telegram_bot import *
import json

def check_event(when):
    if when == "Today":
        when_date = datetime.date.today().strftime('%d/%m')
        complete_when_date = datetime.date.today().strftime('%d/%m/%Y')
    elif when == "Tomorrow":
        when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m')
        complete_when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        
    with open('events.json', encoding='utf-8') as file:
        data = json.load(file)
    
    event_list=[]
    for event in data['events']:
        if (event['date'][0:5] == when_date) and (event['type'] == "Event"):
            if (event['date'] == complete_when_date) or ((event['date'] != complete_when_date) and (event['recurrency'] == True)):
                print(f"Reminder for today: {event['name']}!")
                event_list.append(event['name'])

    if len(event_list) == 0:
        return()
    else:
        send_telegram_msg(when, complete_when_date, event_list, "null")  
        
def check_birthday(when):
    if when == "Today":
        when_date = datetime.date.today().strftime('%d/%m')
        complete_when_date = datetime.date.today().strftime('%d/%m/%Y')
    elif when == "Tomorrow":
        when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m')
        complete_when_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        
    with open('events.json', encoding='utf-8') as file:
        data = json.load(file)
    
    name_list=[]
    count_list=[]
    for event in data['events']:
        if (event['date'][0:5] == when_date) and (event['type'] == "Birthday"):
            count=str(int(datetime.date.today().strftime('%Y'))-int(event['date'][6:]))
            print(f"{when} is {event['name']}'s birthday ({count})!")
            name_list.append(event['name'])
            count_list.append(count)

    if len(name_list) == 0:
        return()
    else:
        send_telegram_msg(when, complete_when_date, name_list, count_list)
            
### PROGRAM ###
check_birthday("Today")
check_birthday("Tomorrow")
check_event("Today")
check_event("Tomorrow")