import json
import time
import requests
import conf
import datetime
import time_count

currentDT = datetime.datetime.now()

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%dh %02dm %02ds" % (hour, minutes, seconds) 

total_time=int(time_count.end_time)-int(time_count.start_time)
total_execution_time=convert(total_time)

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

line1 = "Alert! Havoc-OS test build {build_name} for Moto G5 Plus (potter) completed at " + currentDT.strftime("%d-%m-%Y %H:%M:%S IST.\n")
line2 = "Duration : " + total_execution_time
line3 = "\nBuild available at https://abhi-cloud.dyndns.org/index.php/s/1JgFedmXz3I5m3Q . "
message = line1 + line2 + line3
telegram_status = send_telegram_message(message)
print("This is the Telegram status:", telegram_status)