

import asyncio
import random, re
import datetime
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.utils import admin_cmd
from var import Var
telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


@borg.on(admin_cmd(pattern="recognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Reply to any user's media message.")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("reply to media file")
       return
    chat = "@Rekognition_Bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Reply to actual users message.")
       return
    cat = await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.edit("unblock @Rekognition_Bot and try again")
              await cat.delete()
              return
          if response.text.startswith("See next message."):
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              response = await response
              cat = response.message.message
              await event.edit(cat)
      
          else:
              await event.edit("sorry, I couldnt find it")
              

@borg.on(admin_cmd(pattern="instadl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    chat = "allsaverbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Opening 😅😅```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=804576054))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=804576054))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=804576054))
              await asyncio.sleep(3)
              await event.client.forward_messages(chat, reply_message)
              await asyncio.sleep(2)
              response = await response
              response = await response2 
              response = await response3
          except YouBlockedUserError: 
              await asyncio.sleep(3)
              await event.reply("```Please unblock (allsaverbot) ```")
              return
          if response.text.startswith("Hi!"):
             await asyncio.sleep(3)
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 
             await asyncio.sleep(3)
             await event.delete()
             await asyncio.sleep(2)
             await event.client.send_message(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="wspr ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()



@borg.on(admin_cmd(pattern="purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FiletolinkTGbot"
    reply_message.sender
    await event.edit("**Making public url...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1011636686)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("```Please unblock me (@FiletolinkTGbot) u Nigga```")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )
  

@borg.on(admin_cmd(pattern="limits ?(.*)"))
async def _(event):
    bot = "@SpamBot"
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                danish = await conv.get_response()
                final = ("HeHe", "")
                await borg.send_message(event.chat_id, danish.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @spambot `and retry!")




CMD_HELP.update(
    {
        "bots": ".purl <reply to file>\nUse - Get a direct download link of that file/doc/pic/vid\
        \n\n.instadl <reply to instagram url>\\nUse - Download that instagram post.\
        \n\n.recognize <reply to any media>\\nUse - send details about it.\
        \n\n.wspr <message> <target username/id>\nUse - Send a whisper message to that person.\
        \n\n.limits\nUse - Check if you are limited by telegram."
    }
)
