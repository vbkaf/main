import asyncio
import logging
import random
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = '7587555755:AAEU4ryiwPqOIDn-vEwdIBbUUWjbCSuNREg'

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(CommandStart())
async def Start(message: Message):
    await message.answer(f'Здаров пидор \nIP : {html.spoiler(random.randint(0,256))}.
                         {html.spoiler(random.randint(0,256))}.
                         {html.spoiler(random.randint(0,256))}.
                         {html.spoiler(random.randint(0,256))}')

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())    