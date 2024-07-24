from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hlink



router = Router()

reviews = hlink('Оставить отзыв', 'https://clck.ru/3C6MBm')
manager = hlink('Написать нам', 'https://t.me/barista_chef')


@router.message(F.text == '☎️Контакты')
async def get_contact(message: Message):
    await message.answer(
        '<b>Контакты:</b>\n'
        '\n'
        '☎️ <b>Телефон:</b> +7 (969) 238-48-88\n'
        '\n'
        f'📝 <b>Отзывы:</b> {reviews}\n'
        '\n'
        f'💬 <b>Менеджер:</b> {manager}\n'
        '\n',
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


@router.message(F.text == '😉Пригласить друга')
async def get_ref(message: Message):
    await message.answer(
        'Здесь будет реферальная система'
    )


@router.message(F.text == '🛒Мои заказы')
async def get_order(message: Message):
    await message.answer(
        'В данный момент у вас нет активных заказов в нашем магазине.'
        'Чтобы открыть магазин введите команду - /shop'
    )



