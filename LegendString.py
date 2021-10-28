import os
os.system("pip install telethon")
import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


okvai = input("Enter junta to continue: ")
if okvai == "junta":
    print("Please go to my.telegram.org and get your API Id and API Hash to proceed.")
    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        print(client.session.save())
        print("check your save message ")
        client.send_message("me", client.session.save())
        client.send_message("me", "Above is your #JUNTA STRING SESSION ,,, kelay yalew yerso #JUNTA USERBOT STRING SESSION  new yehnen  session lemanm endaysetu \nPaste this string in Heroku Var.\n\n[Developer Abex kos](t.me/JUNTAUSERBOT")

else:
    print("yetesasate neger asgebtewal")
