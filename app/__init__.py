from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Токен бота не найден! Создайте .env файл с BOT_TOKEN")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")