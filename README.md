# Birthday/Event Reminder Bot
Bot that remembers birthdays and sends a telegram message with the notice.
<img src="https://github.com/amuracciole/birthday_reminder/blob/main/cake_gif.gif" width="300" height="300">
<img src="https://github.com/amuracciole/birthday_reminder/blob/main/reminder_gif.gif" width="300" height="300">

## Keys :key:
Plese add you own Telegram keys

## Run: :computer:
<img src="https://github.com/amuracciole/birthday_reminder/blob/main/web.png" width="700" height="300">
To interact with the bot, you have 2 options:
- A menu which is executed with the command "python menu.py". 
- Web interface running in http://localhost:2600 and  consumes API resources on port 2601
Both allows you to add and remove birthdays and events to the list, as well as display it.

## Run API server: :zap:
To run the API and web server, please run python3 run.py

## Crontab :stopwatch:
You MUST include the following line in you crontab file to run the script every day at 10:00 AM (You can schedule as you wish)

0 10 * * * *project path*

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/amuracciole)