class TelegramView:
    """Класс для генерации Telegram-сообщений."""

    @staticmethod
    def ask_for_file() -> str:
        return "📁 Пожалуйста, загрузите файл договора (PDF/DOCX)"

    @staticmethod
    def format_response(text: str) -> str:
        return f"📝 Результат анализа:\n\n{text}"