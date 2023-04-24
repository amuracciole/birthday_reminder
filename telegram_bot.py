#!/usr/bin/env python3
import requests
import config

# https://www.youtube.com/watch?v=M9IGRWFX_1w&ab_channel=BaoLuThe

def send_telegram_msg(today, names, count):
    token=config.TELEGRAM_TOKEN
    chat_id = config.TELEGRAM_CHAT_ID
    text_1 = "🎂 Today ({}) is the birthday of:".format(today)
    text_2 = "\n"
    for x in range(0,len(count)):
        text_2 = text_2 + "{} ({})".format(names[x], count[x]) + "\n"
    text=text_1 + text_2
    print (text)
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

