from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from core.config import settings

router = Router()

@router.message(Command("parserun"))
async def parserun_cmd(message: Message):
    if message.from_user.id != settings.allowed_user_id:
        await message.answer("⛔ Доступ запрещён.")
        return
    await message.answer("🔍 Парсинг запущен! Ищу проекты...")
    # Здесь будет вызов парсинга
    from bot.handlers.parse import start_parse_task
    await start_parse_task(message, None)  # временно без состояния
