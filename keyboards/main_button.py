from aiogram import types
from aiogram.types import WebAppInfo


kb = [
    [
        types.KeyboardButton(text='🛍Магазин',
                             web_app=WebAppInfo(url=f'https://cafeburgersmoscow.ru')),
        types.KeyboardButton(text='☎️Контакты'),

    ],
]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
