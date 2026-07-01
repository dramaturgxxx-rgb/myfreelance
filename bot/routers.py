from aiogram import Router
from bot.handlers.start import router as start_router
from bot.handlers.parse import router as parse_router  # если есть
# ... другие импорты

router = Router()
router.include_router(start_router)
router.include_router(parse_router)
# ... и другие
