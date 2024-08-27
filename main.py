import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import  CommandStart, Command

bot = Bot(token="7421036125:AAEJ6atnRLC-BvP465ZCavHjMV96nd9R2QQ")
dp = Dispatcher()


@dp.message()
async def cmd_start(message: Message):
    await message.answer("hi")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
