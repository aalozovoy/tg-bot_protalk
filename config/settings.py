import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Основные настройки
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PROCUREMENT_API_KEY = os.getenv("PROCUREMENT_API_KEY")

    # Google Sheets (статья: https://vc.ru/ai/1455895)
    GOOGLE_SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS_JSON")

    # Безопасность (статья: https://habr.com/ru/articles/820461/)
    ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # Для уведомлений