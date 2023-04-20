import datetime
from birthdays import birthdays_list
from telegram_bot import *

def check_birthday():
    today = datetime.date.today().strftime('%d-%m-%Y')
    name_list=[]
    for name, date in birthdays_list.items():
        if date == today:
            print(f"Today is {name}'s birthday!")
            name_list.append(name)
    string_name_list = "\n".join(name_list)
    print(string_name_list)
    send_telegram_msg(today, string_name_list)
    
### PROGRAM ###
check_birthday()