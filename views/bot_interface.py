from telegram import Update, ReplyKeyboardMarkup, Document
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import Config
from controllers.contract_controller import ContractController


class TelegramBot:
    def __init__(self):
        self.app = Application.builder().token(Config.BOT_TOKEN).build()
        self._setup_handlers()

    def _setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, _):
        keyboard = [["📄 Анализ договора", "🔍 Поиск закупок"]]
        await update.message.reply_text(
            "Добро пожаловать! Выберите действие:",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    async def handle_document(self, update: Update, _):
        """Обработка документа для кнопки 1 (статья: https://habr.com/ru/articles/861770/)."""
        file: Document = await update.message.document.get_file()
        await file.download_to_drive("user_contract.docx")
        analysis_result = ContractController.analyze_contract("user_contract.docx")
        await update.message.reply_text(f"Результат анализа:\n{analysis_result}")