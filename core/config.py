from pydantic_settings import BaseSettings
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # Используем getenv с пустым значением по умолчанию, чтобы не падать
    telegram_token: str = os.getenv("TELEGRAM_TOKEN", "")
    allowed_user_id: int = int(os.getenv("ALLOWED_USER_ID", "1700036328"))
    system_message: str = os.getenv(
        "SYSTEM_MESSAGE",
        "СТРОГОЕ ПРАВИЛО: Ты помощник для Данила, который отвечает на задания на фрилансе. ВСЕГДА формируй отклик от первого лица, в деловом официальном стиле, как если бы я, Данил, лично писал заказчику. Ни при каких условиях не используй смайлики, не задавай вопросы, не говори 'готов помочь', не вставляй код, списки или Markdown.  Отклик должен сразу объяснять, как я выполню задание, включая технологии и библиотеки.  Пример правильного отклика, которому нужно следовать по стилю:\n\n Здравствуйте.\n\n Готов выполнить разработку программного решения для парсинга публикаций из социальных сетей.\n\nОписание решения:\nПрограмма будет автоматически собирать новые посты (текст и изображения) из выбранных источников: Instagram, Telegram и ВКонтакте. Система может работать как с использованием официальных API, так и через обходные методы (HTML-парсинг, Selenium) при необходимости.\n\nОсновная логика работы:\nФормируется список источников для мониторинга с указанием категорий. Парсер проверяет наличие новых публикаций по расписанию. Информация сохраняется в базе данных. Реализуется возможность экспорта данных и, при необходимости, веб-интерфейс.\n\nТехническая реализация: Python, библиотеки Telethon, vk_api, Instaloader или Selenium; база данных PostgreSQL или MongoDB.\n\nСвязь для уточнения деталей: Telegram — @DanilChagarnoy.\n\nМодель должна создавать отклики в таком же формате и стиле для любого задания."
    )
    
    polza_api_key: str = os.getenv("POLZA_API_KEY", "")
    polza_model: str = os.getenv("POLZA_MODEL", "deepseek/deepseek-chat")
    
    pages_from: int = int(os.getenv("PAGES_FROM", "1"))
    pages_to: int = int(os.getenv("PAGES_TO", "1"))
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT", "15"))
    max_retries: int = int(os.getenv("MAX_RETRIES", "2"))
    max_projects: int = int(os.getenv("MAX_PROJECTS", "10"))
    base_search: str = os.getenv(
        "BASE_SEARCH",
        "https://freelance.ru/project/search?q=&a=1&v=1&c%5B0%5D=4&page={}"
    )
    discussion_template: str = os.getenv(
        "DISCUSSION_TEMPLATE",
        "https://freelance.ru/project/discussion/start/{}"
    )
    cookies: str = os.getenv("COOKIES_PATH", "core/cookies/freelance.ru_cookies.txt")
    output_json_result: str = os.getenv("OUTPUT_JSON", "output/freelance_projects_with_responses.json")


settings = Settings()

# Проверка, что токен не пустой (чтобы не запустить бота без токена)
if not settings.telegram_token:
    raise ValueError("TELEGRAM_TOKEN не задан! Укажите его в переменных окружения или файле .env")

bot = Bot(
    token=settings.telegram_token,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
)
