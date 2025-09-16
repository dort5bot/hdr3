import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from config import config
from handlers import upload_handler, status_handler, admin_handler
from utils.logger import setup_logger

# Logger kurulumu
setup_logger()

async def main():
    # Redis storage for FSM
    storage = RedisStorage.from_url(config.REDIS_URL)
    
    bot = Bot(
        token=config.TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)
    
    # Handlers'ı kaydet
    dp.include_router(upload_handler.router)
    dp.include_router(status_handler.router)
    dp.include_router(admin_handler.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
