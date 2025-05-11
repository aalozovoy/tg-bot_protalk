from app.models.procurement_model import ProcurementModel
from app.views.telegram_view import TelegramView
from app.services.parser_service import ParserService


class ProcurementController:
    """Контроллер для обработки запросов по закупкам (Кнопка 2)."""

    def __init__(self):
        self.model = ProcurementModel()
        self.view = TelegramView()
        self.parser = ParserService()

    def handle_procurement_request(self, user_input):
        """
        Обрабатывает запрос на поиск закупок по перечню продукции.

        Args:
            user_input (str): Перечень товаров/услуг от клиента.

        Returns:
            str: Результат поиска закупок в формате Markdown.
        """
        if not user_input:
            return self.view.ask_for_input(
                "Укажите перечень товаров/услуг для поиска (например: 'трубы стальные, услуги связи')")

        products = self.model.parse_products(user_input)
        results = self.parser.search_procurements(products)

        return self.view.format_procurement_results(results)