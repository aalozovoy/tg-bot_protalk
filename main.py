from telegram.ext import Application, CommandHandler
from app.controllers.contract_controller import ContractController
from app.controllers.procurement_controller import ProcurementController
from app import Config


async def start(update, context):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Добро пожаловать! Используйте:\n"
        "/contract - анализ договора\n"
        "/procurement - поиск закупок"
    )


def start_bot():
    """Инициализация и запуск бота"""
    # Создаем Application
    application = Application.builder().token(Config.BOT_TOKEN).build()

    # Инициализация контроллеров
    contract_ctrl = ContractController()
    procurement_ctrl = ProcurementController()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("contract", contract_ctrl.handle_contract_request))
    application.add_handler(CommandHandler("procurement", procurement_ctrl.handle_procurement_request))

    print("Бот запущен...")
    application.run_polling()


if __name__ == "__main__":
    start_bot()