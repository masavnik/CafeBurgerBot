from aiogram import types
from aiogram.types import WebAppInfo

kb = [
    [
        types.KeyboardButton(text='🛍Магазин',
                             web_app=WebAppInfo(url=f'https://masavnik.github.io/CafeBurgerBot/shop/base.html')),
        types.KeyboardButton(text='🛒Мои заказы')
    ],
    [types.KeyboardButton(text='☎️Контакты')],
]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
