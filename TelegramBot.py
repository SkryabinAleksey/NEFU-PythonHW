import json
import requests
import random

BOT_API_TOKEN = "1002921566:AAFFloIW8ojYVoYnE4x-Rc_jbNDCB8uDxa4"
# Имя бота RandomMessageBot
# Сохраняет сообщения в отдельный файл и в ответ пишет рандомное сообщение из сохраненных

def send_response(user_id, text):
   SEND_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
   CHAT_ID = user_id
   url = SEND_URL.format(
       BOT_API_TOKEN,
       CHAT_ID,
       text
   )
   requests.get(url)

update_id = 0
all_messages = []

def readmyfile():
   global update_id
   global all_messages
   f = open("text.txt", "r")
   update_id = int(f.readline())
   for line in f:
       line = line.strip()
       if line == "":
           break
       user_id, msg = line.split(' ', 1)
       user_id = int(user_id)
       all_messages.append([user_id, msg])
   f.close()

def writemyfile():
   global update_id
   f = open("text.txt", "w")
   print(update_id, file = f)
   for msg in all_messages:
       uid, message = msg
       print("{} {}".format(uid, message), file=f)
   f.close()

if __name__ == '__main__':
    READ_URL = "https://api.telegram.org/bot{}/getUpdates?offset={}"
    url = READ_URL.format(BOT_API_TOKEN, update_id+1)
    response = requests.get(url)
    updates = response.json().get("result", [])
    readmyfile()
    for msg in updates:
        update_id = int(msg["update_id"])
        text = msg["message"]["text"]
        user_id = msg["message"]["from"]["id"]
        all_messages.append([int(user_id), text])
        send_response(user_id, random.choices(text))
    writemyfile()
