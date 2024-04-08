import asyncio

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message

from .help import *


async def progress_callback(current, total, bot: Client, message: Message):
    if int((current / total) * 100) % 25 == 0:
        await message.edit(f"{humanize.naturalsize(current)} / {humanize.naturalsize(total)}")


@Client.on_message(filters.command('upload', '.') & filters.me)
async def upload_helper(bot: Client, message: Message):
    if len(message.command) > 1:
        await bot.send_document('self', message.command[1], progress=progress_callback, progress_args=(bot, message))
    else:
        await message.edit('No 𝚙𝚊𝚝𝚑 𝚙𝚛𝚘𝚟𝚒𝚍𝚎𝚍.')
        await asyncio.sleep(3)

    await message.delete()


add_command_help(
    "➥ 𝐔ᴘʟᴏᴀᴅ",
    [
        [".upload", "Uᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ғʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ꜱʏꜱᴛᴇᴍ ғɪʟᴇ ᴘᴀᴛʜ."],
    ],
)
