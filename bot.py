from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from handlers import user_command, answer_keyboards
import os
import asyncio


async def main():
    # load_dotenv()
    bot = Bot('7395547339:AAHAULBca9ZL10cRSYvijO4kcKc_-oNKk4U')
    dp = Dispatcher()
    dp.include_routers(
        user_command.router,
        answer_keyboards.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())