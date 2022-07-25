import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import SITHIJATD_TEXT, SITHIJATD_BUTTONS

@bot.on_message(filters.regex("@sithijatd"))
async def sithijatdmsg(_, message):
   # m = await message.reply("|( ͡❛ ͜ʖ ͡❛)")
   #     await m.edit("||っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("| |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|  |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|   |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|    |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|     |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|      |っ ͡❛ ͜ʖ ͡❛|っ🧠")
   #     await m.edit("|       |っ ͡❛ ͜ʖ ͡❛|っ🧠") 
   #     await m.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ🧠\n                  🗑")
   #     await m.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ  \n                  🗑")
   #     await m.edit("|        |っ ͡❛ ͜ʖ ͡❛|っ  \n                  💩")
        await message.reply_text(SITHIJATD_TEXT,
        reply_markup=SITHIJATD_BUTTONS,
        disable_web_page_preview=True
)
    # await m.delete()
