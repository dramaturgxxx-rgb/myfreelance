from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("✅ Бот работает! Отправьте /parserun для запуска парсинга.")
