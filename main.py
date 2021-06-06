import discord
import json
import datetime
import time
import os
import random
os.system('cls')
print('''\u001b[36m
 ██▓███   ██▀███   █    ██  ███▄    █ ▓█████ 
▓██░  ██▒▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀ 
▓██░ ██▓▒▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒▒███   
▒██▄█▓▒ ▒▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒██▒ ░  ░░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░░▒████▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░
░▒ ░       ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░
░░         ░░   ░  ░░░ ░ ░    ░   ░ ░    ░   
            ░        ░              ░    ░  ░                                      
''')
with open ("config.json") as s:
    k = json.load(s)
d = k.get("token")
date = datetime.datetime.now()
skid = date.strftime("%D, %H:%M:%S")
client = discord.Client()
@client.event
async def on_connect():
    print('\u001b[32m' + skid + ' | ' + 'Connected:\u001b[34m ' + client.user.name)
@client.event
async def on_message(msg):
    if msg.author == client.user:
        poop = [5, 8, 4, 10, 9]
        time.sleep(random.choice(poop))
        await msg.delete()
        print('\u001b[32m' + skid + ' | ' + 'Message Deleted:\u001b[34m ' + msg.content)
client.run(d, bot=False)