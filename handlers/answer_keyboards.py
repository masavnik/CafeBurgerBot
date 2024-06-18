from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message


router = Router()


@router.message(F.text == '☎️Контакты')
async def get_contact(message: Message):
    await message.answer(
        '<b>Контакты:</b>\n'
        '\n'
        '☎️ <b>Телефон:</b> ВАШ КОНТАКТ\n'
        '\n'
        '📝 <b>Отзывы:</b> Оставить отзыв (Ваша ссылка где будет отзыв)\n'
        '\n'
        '💬 <b>Менеджер:</b> Написать нам (Ваш менеджер)\n'
        '\n'
        'Можете добавить другие контакты',
        parse_mode=ParseMode.HTML
    )


# @router.message(F.text == '🛍Магазин')
# async def get_contact(message: Message):
#     await message.answer(
#         'Будет открываться магазин'
#     )


@router.message(F.text == '🛒Мои заказы')
async def get_contact(message: Message):
    await message.answer(
        'В данный момент у вас нет активных заказов в нашем магазине.'
        'Чтобы открыть магазин введите команду - /shop'
    )


@router.message(F.text == '‍♂️Пригласить друга')
async def get_contact(message: Message):
    await message.answer(
        'Здесь будет риферальная система'
    )