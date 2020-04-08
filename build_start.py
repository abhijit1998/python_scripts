import json
import time
import requests
import conf
import datetime
import build

currentDT = datetime.datetime.now()

def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "GET",
            url,
            params=data
        )
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False


line1="Alert! {} test build for Moto G5 Plus (potter) started at ".format(build.build_name) + currentDT.strftime("%d-%m-%Y %H:%M:%S IST.")
line2="\nJenkins URL: {}console".format(build.build_url)
message = line1+line2
telegram_status = send_telegram_message(message)
print("This is the Telegram status:", telegram_status)
