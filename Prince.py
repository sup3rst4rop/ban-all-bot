from choot import Var
import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


Prince = TelegramClient(None, Var.API_KEY, Var.API_HASH)
Prince.start(bot_token=Var.TOKEN)

print("STARTING BANALL BOT BY PRINCE's SERVER....") 

"""
MOVING TO COMMANDS NOW
"""

GANDU = []
for x in Var.OWNER_ID: 
    GANDU.append(x)


@Prince.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in GANDU:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm Active🔥\nStart Fucking Any Group** \n\n **__ᏢᎾᏁᎶ🏓__ !!** `{ms}` ms")

"""
 RESTART COMMANDS 
"""
@Prince.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in GANDU:
        text = "Ma Chud Gai Iski Vro🤣....!!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Prince.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

"""
 BANALL COMMAND
"""
 
@Prince.on(events.NewMessage(pattern="^/banall"))
async def testing(event):
  if event.sender_id in GANDU:
   if not event.is_group:
        Reply = f"Noob !! Use This Cmd in Group."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       Superstar = await event.get_chat()
       Superstar = await event.client.get_me()
       admin = Superstar.admin_rights
       creator = Superstar.creator
       if not admin and not creator:
           await event.reply("I Don't have sufficient Rights !!")
           return
       await event.reply("**Superstar Begins...**")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == Superstar.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


"""
  LEAVE COMMAND 
"""
print("Leave Command Soon Currently Am Busy") 
print("STARTED SUCCESSFULLY... JOIN @about_sup3r_st4r") 
Prince.run_until_disconnected()
