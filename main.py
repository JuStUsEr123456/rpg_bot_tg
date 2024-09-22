import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from handlers import reg, commands, fighting
from aiogram_sqlite_storage.sqlitestore import SQLStorage


from aiogram import Bot, Dispatcher
load_dotenv()


# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("TOKEN")

my_storage = SQLStorage('rpg.db', serializing_method='pickle')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher(storage=my_storage)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN)
    # And the run events dispatching
    dp.include_routers(
        commands.router,
        reg.router,
        fighting.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())