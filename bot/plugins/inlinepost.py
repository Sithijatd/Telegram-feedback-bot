from bot import bot
from pyrogram import filters, idle
from pyrogram.types import (InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)


#------------------------variables-------------------------------
HYPERTXT = """<b>Hey, friends🙋‍♂</b>
<b>☘️We are Hyper Design.
Invite all designing loves to join with us.☘️</b>
✨<i>Learn Designing</i>
✨<i>Free Logos</i>
✨<i>PLP Files</i>
✨<i>Giveaways</i>
    Be Creative Be We
〣────────────〢
         Creative We
  <b>⚡️Hyper Designs🤟</b>
〢────────────〣"""

BOTIMG='https://telegra.ph/file/60d0d641d96d9cdccf8a9.jpg'
BOTBTNS = InlineKeyboardMarkup(
                               [
                                [InlineKeyboardButton(text='Visit Bot', url='https://t.me/imsithijabot')],
                                [InlineKeyboardButton(text='Open MEnu', callback_data='startmenu')]
                               ]
                               )
HYPERBTNS = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('⚡️Hyper Designs🤟' , url='https://t.me/HyperDesigns')
                ],
                [
                  InlineKeyboardButton('👥 Group 👥' , url='https://t.me/HyperDesignsChat'),
                ], 
                [
                  InlineKeyboardButton('🔰Share post🔰' , switch_inline_query=""),
                ], 
                [
                 InlineKeyboardButton('〣────────────────〢' , callback_data='postcall'),
                ],

              ]
)
#----------------------variables end-----------------------------
@bot.on_callback_query(filters.regex("postcall"))
async def postcallbacc(_, CallbackQuery):
    await bot.answer_callback_query(CallbackQuery.id, text="🔆Shared Via @ImSithijaBot...", show_alert=False)

@bot.on_inline_query()
async def answer(_, inline_query):
   if inline_query.query=='':
        await inline_query.answer(
            results=[
            InlineQueryResultPhoto(
                title=f"Hყρҽɾ Ɗҽʂιɠɳʂ |🇱🇰",
                description="Click Here",
                photo_url="https://telegra.ph/file/60d0d641d96d9cdccf8a9.jpg",
                thumb_url="https://telegra.ph/file/60d0d641d96d9cdccf8a9.jpg",
                caption=HYPERTXT,
                reply_markup=HYPERBTNS,
                ),
            ],
        cache_time=1
        )
