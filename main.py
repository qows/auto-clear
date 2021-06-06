# -*- coding: utf-8 -*-
import discord, json, random, json, datetime, time, os
os.system("cls" if os.name == "nt" else "clear")
print('██▓███   ██▀███   █    ██  ███▄    █ ▓█████\n▓██░  ██▒▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀\n▓██░ ██▓▒▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒▒███  \n▒██▄█▓▒ ▒▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄\n▒██▒ ░  ░░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░░▒████▒\n▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░\n░▒ ░       ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░\n░░         ░░   ░  ░░░ ░ ░    ░   ░ ░    ░   \n            ░        ░              ░    ░  ░')
with open ("config.json") as l:
    j = json.load(l)
j = t.get("token")
h = datetime.datetime.now()
d = date.strftime("%D, %H:%M:%S")
client = discord.Client()
@client.event
async def on_connect():
    print('\u001b[32m' + t + ' | Connected:\u001b[34m ' + client.user.name)
@client.event
async def on_message(msg):
    if msg.author == client.user:
        n = [5, 6, 7, 8, 9, 10] # maybe ill open other pull req changing this for get a random number from 5 to 8, not hard i think ( i mean like randommath)
        time.sleep(random.choice(n))
        await msg.delete()
        print('\u001b[32m' + t + ' | Messeage Deleted:\u001b[34m ' + msg.content)
client.run(t, bot=False)
