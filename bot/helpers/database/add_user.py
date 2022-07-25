import os
from bot.helpers.database.access_db import db
from pyrogram import Client
from config import Config
from pyrogram.types import Message

async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"**📢 News**\n\n**#NEW_USER Started To #PmBot**\n\n**New User** [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n **User Id**- {cmd.from_user.id} \n **Started @ImSithijabot 🚀**"
            )

