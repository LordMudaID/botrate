# button.py

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUBS_CHANNEL_2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    buttons = [
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ]

    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons.insert(1, [InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(1, [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2)
        ])

    if FORCE_SUBS_CHANNEL_2 and not FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3)])

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2)])

    return buttons


def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2)
        ])

    if FORCE_SUBS_CHANNEL_2 and not FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelink3)])

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2)])

    try:
        buttons.append([
            InlineKeyboardButton(
                text="ᴄᴏʙᴀ ʟᴀɢɪ",
                url=f"https://t.me/{client.username}?start={message.command[1]}",
            )
        ])
    except IndexError:
        pass

    return buttons
