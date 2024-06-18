from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.main_button import keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f'Приветствую! Я - твой персональный бот для заказа вкусной еды. '
        f'Давай порадуем тебя сочными бургерами и вкусными завтраками! '
        f'Жми кнопку "Магазин"',
        reply_markup=keyboard
    )



