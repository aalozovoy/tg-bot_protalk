from telegram import Update
from telegram.ext import CallbackContext
from app.models.contract_model import ContractModel
from app.views.telegram_view import TelegramView
from app.services.ai_service import AIService


class ContractController:
    """Контроллер для обработки запросов по составлению договоров."""

    def __init__(self):
        self.model = ContractModel()
        self.view = TelegramView()
        self.ai = AIService()

    async def handle_contract_request(self, update: Update, context: CallbackContext):
        """Асинхронный обработчик команды /contract"""
        if not update.message.document:
            await update.message.reply_text(self.view.ask_for_file())
            return

        # Здесь должна быть логика загрузки файла
        file = await update.message.document.get_file()
        file_content = await file.download_as_bytearray()

        analysis_result = self.model.analyze_contract(file_content)
        response = self.view.format_response(analysis_result)

        await update.message.reply_text(response)