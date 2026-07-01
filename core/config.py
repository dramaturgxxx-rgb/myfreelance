import os
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Все переменные через getenv с запасным значением
    telegram_token = os.getenv("TELEGRAM_TOKEN", "")
    allowed_user_id = int(os.getenv("ALLOWED_USER_ID", "1700036328"))
    system_message = os.getenv(
        "SYSTEM_MESSAGE",
        "СТРОГОЕ ПРАВИЛО: Ты помощник для Данила, который отвечает на задания на фрилансе. ВСЕГДА формируй отклик от первого лица, в деловом официальном стиле, как если бы я, Данил, лично писал заказчику. Ни при каких условиях не используй смайлики, не задавай вопросы, не говори 'готов помочь', не вставляй код, списки или Markdown. Отклик должен сразу объяснять, как я выполню задание, включая технологии и библиотеки."
    )
    polza_api_key = os.getenv("POLZA_API_KEY", "")
    polza_model = os.getenv("POLZA_MODEL", "deepseek/deepseek-chat")
    
    pages_from = int(os.getenv("PAGES_FROM", "1"))
    pages_to = int(os.getenv("PAGES_TO", "1"))
    request_timeout = int(os.getenv("REQUEST_TIMEOUT", "15"))
    max_retries = int(os.getenv("MAX_RETRIES", "2"))
    max_projects = int(os.getenv("MAX_PROJECTS", "10"))
    base_search = os.getenv("BASE_SEARCH", "https://freelance.ru/project/search?q=&a=1&v=1&c%5B0%5D=4&page={}")
    discussion_template = os.getenv("DISCUSSION_TEMPLATE", "https://freelance.ru/project/discussion/start/{}")
    cookies = os.getenv("COOKIES_PATH", "core/cookies/freelance.ru_cookies.txt")
    output_json_result = os.getenv("OUTPUT_JSON", "output/freelance_projects_with_responses.json")

settings = Settings()

# Проверка, что токен задан (иначе бот не запустится)
if not settings.telegram_token:
    raise ValueError("❌ TELEGRAM_TOKEN не задан! Укажите его в переменных окружения или .env")

# Создаём объект бота
bot = Bot(
    token=settings.telegram_token,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
