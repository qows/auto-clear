# -*- coding: utf-8 -*-
import discord, json, random, datetime, time, os
os.system("cls" if os.name == "nt" else "clear")
print('\u001b[34m██▓███   ██▀███   █    ██  ███▄    █ ▓█████\n▓██░  ██▒▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀\n▓██░ ██▓▒▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒▒███  \n▒██▄█▓▒ ▒▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄\n▒██▒ ░  ░░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░░▒████▒\n▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░\n░▒ ░       ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░\n░░         ░░   ░  ░░░ ░ ░    ░   ░ ░    ░   \n            ░        ░              ░    ░  ░')
with open ("config.json") as l:
    j = json.load(l)
t = j.get("token")
h = datetime.datetime.now()
d = h.strftime("%D, %H:%M:%S")
client = discord.Client()
@client.event
async def on_connect():
    print('\u001b[32m' + d + ' | Connected:\u001b[34m ' + client.user.name)
@client.event
async def on_message(msg):
    if msg.author == client.user:
        n = [4, 5, 6, 7, 8] 
        time.sleep(random.choice(n))
        await msg.delete()
        print('\u001b[32m' + d + ' | Messeage Deleted:\u001b[34m ' + msg.content)
client.run(t, bot=False)
