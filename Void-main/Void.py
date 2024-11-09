import pystyle
import requests
import json
import os
from pystyle import Colorate, Colors, Center

logo = f"""
██    ██  ██████  ██ ██████  
██    ██ ██    ██ ██ ██   ██ 
██    ██ ██    ██ ██ ██   ██ 
 ██  ██  ██    ██ ██ ██   ██ 
  ████    ██████  ██ ██████  
                             
"""

with open("input/tokens.txt", "r") as f:
    tokens = f.read().splitlines()

def Spammer():
    def Send(token, id, msg):
        headers = {"authorization": token}
        url = f"https://discord.com/api/v10/channels/{id}/messages"

        r = requests.post(url, headers=headers, json={"content": msg})

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"[Success] {(token[:-5] + '*****')}"))
        else:
            print(Colorate.Color(Colors.red, f"[Failed] {(token[:-5] + '*****')} {r.status_code}"))
    
    channel_id = input(Colorate.Color(Colors.blue, "Enter the channel id: "))
    msg = input(Colorate.Color(Colors.blue, "Enter the message: "))

    while True:
        for token in tokens:
            Send(token, channel_id, msg)

def Webhookspammer():
    def send(webhook, msg):
        r2 = requests.get(webhook).json()
        name = r2.get('name', 'Unknown Webhook')
        r = requests.post(webhook, json={"content": msg})

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"[Success] {name}"))
        else:
            print(Colorate.Color(Colors.red, f"[Failed] {name} {r.status_code}"))

    webhook = input(Colorate.Color(Colors.blue, "Enter the webhook: "))
    msg = input(Colorate.Color(Colors.blue, "Enter the message: "))

    while True:
        send(webhook, msg)

def WebhookDeleter():
    def Delete(webhook):
        r2 = requests.get(webhook).json()
        name = r2.get('name', 'Unknown Webhook')
        r = requests.delete(webhook)

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"[Success] {name}"))
        else:
            print(Colorate.Color(Colors.red, f"[Failed] {name} {r.status_code}"))

    webhook = input(Colorate.Color(Colors.purple, "Enter the webhook: "))
    Delete(webhook)

def TokenChecker():
    def Check(token):
        headers = {"authorization": token}
        url = 'https://discord.com/api/v10/users/@me'

        r = requests.get(url, headers=headers)

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"Valid Token: {(token[:-5] + '*****')}"))
        else:
            print(Colorate.Color(Colors.red, f"Invalid Token: {(token[:-5] + '*****')}"))

    for token in tokens:
        Check(token)

def TokenInfo():
    def Get(token):
        headers = {"authorization": token}
        url = 'https://discord.com/api/v10/users/@me'

        r = requests.get(url, headers=headers)
        print(Colorate.Color(Colors.purple, json.dumps(r.json(), indent=4)))

    token = input(Colorate.Color(Colors.purple, "Enter the token: "))
    Get(token)

def WebhookInfo():
    def Get(webhook):
        r = requests.get(webhook)
        print(Colorate.Color(Colors.purple, json.dumps(r.json(), indent=4)))

    webhook = input(Colorate.Color(Colors.purple, "Enter the webhook: "))
    Get(webhook)

def Leaver():
    def Leave(token, serverid):
        headers = {"authorization": token}
        url = f"https://discord.com/api/v10/users/@me/guilds/{serverid}"

        r = requests.delete(url, headers=headers)

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"[Success] {(token[:-5] + '*****')}"))
        else:
            print(Colorate.Color(Colors.red, f"[Failed] {(token[:-5] + '*****')}"))

    serverid = input(Colorate.Color(Colors.purple, "Enter the server id: "))
    for token in tokens:
        Leave(token, serverid)

def Joiner():
    print(Colorate.Color(Colors.yellow, "THIS JOINER DOES NOT SOLVE CAPTCHA"))

    def Join(token, invite_code):
        url = f"https://discord.com/api/v10/invites/{invite_code}"
        headers = {"authorization": token}

        r = requests.post(url, headers=headers)

        if r.status_code in [200, 201, 202, 203, 204]:
            print(Colorate.Color(Colors.green, f"[Success] {(token[:-5] + '*****')}"))
        else:
            print(Colorate.Color(Colors.red, f"[Failed] {(token[:-5] + '*****')}"))

    code = input(Colorate.Color(Colors.purple, "discord.gg/"))
    for token in tokens:
        Join(token, code)

def ServerInfo():
    def Get(token, id):
        url = f'https://discord.com/api/v10/guilds/{id}'
        headers = {"authorization": token}

        r = requests.get(url, headers=headers)
        print(Colorate.Color(Colors.purple, json.dumps(r.json(), indent=4)))

    id = input(Colorate.Color(Colors.purple, "Enter the Server id: "))
    token = input(Colorate.Color(Colors.purple, "Enter the token: "))
    Get(token, id)

def TokenFormatter():
    def Format(token):
        with open("output/formattedtokens.txt", "a") as f:
            f.write(token[:-5] + "*****\n")

    for token in tokens:
        Format(token)

    file_path = os.path.join(os.path.dirname(__file__), "output", "formattedtokens.txt")
    os.startfile(file_path)

print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(logo)))

menu_options = [
    "1 Spammer              6 Webhook Info",
    "2 Webhook Spammer      7 Leaver",
    "3 Webhook Deleter      8 Joiner",
    "4 Token Checker        9 Server Info",
    "5 Token Info           10 Token Formatter"
]

for option in menu_options:
    print(Colorate.Color(Colors.purple, option))

maininp = input(Colorate.Color(Colors.blue, "Selected Choice -> "))

options = {
    '1': Spammer,
    '2': Webhookspammer,
    '3': WebhookDeleter,
    '4': TokenChecker,
    '5': TokenInfo,
    '6': WebhookInfo,
    '7': Leaver,
    '8': Joiner,
    '9': ServerInfo,
    '10': TokenFormatter,
}

if maininp in options:
    options[maininp]()
else:
    print(Colorate.Color(Colors.red, "Invalid choice!"))
