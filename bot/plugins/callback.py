import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import START_IMG, LOGO_TEXT, LOGO_BUTTON, TOOLS_BUTTON, TOOLS_TEXT, HELP_TEXT, HELP_BUTTON, BOTSTATUS_TEXT, BOTSTATUS_BUTTON, QUOTE_TEXT, QUOTE_BUTTON, SONG_TEXT, SONG_BUTTON


@bot.on_callback_query(filters.regex("logomenu"))
async def logomenu(_, query: CallbackQuery):
    await query.edit_message_text(LOGO_TEXT,
        reply_markup=LOGO_BUTTON,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("quotemenu"))
async def quotemenu(_, query: CallbackQuery):
    await bot.answer_callback_query(query.id, text="💬Quote help...", show_alert=False)
    await query.edit_message_text(QUOTE_TEXT,
        reply_markup=QUOTE_BUTTON,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("songmenu"))
async def songmenu(_, query: CallbackQuery):
    await bot.answer_callback_query(query.id, text="🎧Song downloader...", show_alert=False)
    await query.edit_message_text(SONG_TEXT,
        reply_markup=SONG_BUTTON,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("toolmenu"))
async def toolsmenu(_, query: CallbackQuery):
    await bot.answer_callback_query(query.id, text="🧰More tools...", show_alert=False)
    await query.edit_message_text(TOOLS_TEXT,
        reply_markup=TOOLS_BUTTON,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("wall_gen"))
async def wall_callbacc(_, CallbackQuery):
    await bot.answer_callback_query(CallbackQuery.id, text="✔️Add in soon. . .", show_alert=False)

