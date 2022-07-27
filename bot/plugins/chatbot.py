"""
MIT License

Copyright (c) 2021 Tinura Dinith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
from os import getenv
from bot import bot
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from googletrans import Translator
from pyrogram import enums

async def bot_msg_chatinfo():
    stats = f"""
ℹ️This is a feature of this botℹ️
So this message not send by the sithija.
@ItsMeSithija
"""
    return stats

@bot.on_callback_query(filters.regex("chatb_"))
async def chatinfo_callbacc(_, CallbackQuery):
    text = await bot_msg_chatinfo()
    await bot.answer_callback_query(CallbackQuery.id, text, show_alert=True)

tr = Translator()

@bot.on_message(
    filters.text 
    & filters.private 
    & ~filters.edited 
    & ~filters.bot 
    & ~filters.user(Config.OWNER)
    & ~filters.channel 
    & ~filters.forwarded,
    group=1)
async def chatbot(_, message):
    if message.text[0] == "/":
        return
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    lang = tr.translate(message.text).src
    trtoen = (message.text if lang=="en" else tr.translate(message.text, dest="en").text).replace(" ", "%20")
    text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
    affiliateplus = requests.get(f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=Sithija's%20Assistant&ownername=Sithija%20Dewmina&name=Sithija&master=Sithija%20Dewmina&build=Sithija%20Dewmina&job=Working%20for%20sithija&scmaster=Sithija&user=1")
    textmsg = (affiliateplus.json()["message"])
    msg = tr.translate(textmsg, src='en', dest=lang)
    await message.reply_text(msg.text,
                            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("❕Info❕", callback_data="chatb_")
                            ],
                        ]
                    )
                )
