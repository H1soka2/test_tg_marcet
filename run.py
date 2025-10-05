import asyncio
import logging
import os
from aiogram import Bot,Dispatcher

from app.client import client
from app.database.models import init_models

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s' )


async def main():
    bot = Bot(token='7810300467:AAEKfomILsGO-mzSdmBHpVWsGh17MYTSdOs')
    dp = Dispatcher()
    dp.include_router(client)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


async def startup():
    await init_models()
    logging.info('bot start app...')


async def shutdown(dispatcher:Dispatcher):
    logging.info('Bot shutting down...')





if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('bot stop')