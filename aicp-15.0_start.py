import json
import time
import requests
import conf
import datetime

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



message = "Alert! AICP-15.0 test build for Moto G5 Plus (potter) started at " + currentDT.strftime("%d-%m-%Y %H:%M:%S IST.")
#message = "https://sourceforge.net/projects/unofficial-builds/files/DO-NOT-DOWNLOAD/aicp_potter_p-15.0-UNOFFICIAL-"+currentDT.strftime("%Y%m%d")+".zip/download"
telegram_status = send_telegram_message(message)
print("This is the Telegram status:", telegram_status)