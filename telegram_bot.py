#!/usr/bin/env python3
import requests
import config

# https://www.youtube.com/watch?v=M9IGRWFX_1w&ab_channel=BaoLuThe

def send_telegram_msg(today, names):
    token=config.TELEGRAM_TOKEN
    chat_id = config.TELEGRAM_CHAT_ID
    text = "🎂 Today ({}) is the birthday of:\n{}".format(today, names)
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

