import datetime
from birthdays import birthdays_list
from events import events_list
from telegram_bot import *

def check_birthday():
    today = datetime.date.today().strftime('%d/%m')
    complete_today = datetime.date.today().strftime('%d/%m/%Y')
    name_list=[]
    count_list=[]
    for name, date in birthdays_list.items():
        if date[:5] == today:
            count=str(int(datetime.date.today().strftime('%Y'))-int(date[6:]))
            print(f"Today is {name}'s birthday ({count})!")
            name_list.append(name)
            count_list.append(count)
    #print(string_name_list,len(string_name_list))
    if len(name_list) == 0:
        exit()
    else:
        send_telegram_msg(complete_today, name_list, count_list)

def check_events():
    today = datetime.date.today().strftime('%d/%m')
    complete_today = datetime.date.today().strftime('%d/%m/%Y')
    event_list=[]
    for name, date in events_list.items():
        if date[:5] == today:
            print(f"Reminder for today: {name}!")
            event_list.append(name)
    string_event_list = "\n".join(event_list)
    #print(string_name_list,len(string_name_list))
    if len(string_event_list) == 0:
        exit()
    else:
        send_telegram_msg(complete_today, string_event_list)   

### PROGRAM ###
check_birthday()
check_events()