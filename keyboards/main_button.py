from aiogram import types
from aiogram.types import WebAppInfo
import link

kb = [
    [
        types.KeyboardButton(text='🛍Магазин', web_app=WebAppInfo(url=f'{link}')),
        types.KeyboardButton(text='🛒Мои заказы')
    ],
    [types.KeyboardButton(text='☎️Контакты')],
    [types.KeyboardButton(text='🙋‍♂️Пригласить друга')],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
