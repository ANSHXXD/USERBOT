from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, SDICTATOR
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio 

REPLY_RAID = []

@Client.on_message(filters.command & filters.me)
async def (xspam: Client, message: Message):  
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(SDICTATOR)),
            reply_to=event.message.id,
        )

@Client.on_message(filters.command("rraid", cmd) & filters.me)
async def rraid(xspam: Client, message: Message):  
    if e.sender_id in OWNER_ID:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
                   if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» ᴛʜɪᴋ ʜᴀɪ ʙʜᴀɪ ʙᴏʟɴᴇ ᴅᴏ ᴇs ᴍᴄ ᴋᴏ !! ✅")
        except NameError:
            await e.reply("» .rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>"


@Client.on_message(filters.command("drraid", cmd) & filters.me)
async def drraid(xspam: Client, message: Message):  
    if e.sender_id in OWNER_ID:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ᴛʜɪᴋ ʜᴀɪ ᴍᴀғ ᴋᴀʀ ʀʜᴇ ʜᴀɪ !! ✅")
        except NameError:
            await e.reply( "» .drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » .drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


add_command_help(
    "➥ 𝐑ᴇᴘʟʏʀᴀɪᴅ",
    [
        ["rraid", "start rraid."],
        ["drraid", "remove rraid"],
    ],
  )
