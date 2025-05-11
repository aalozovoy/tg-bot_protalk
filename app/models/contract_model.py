from typing import Dict, Any
from app.services.ai_service import AIService


class ContractModel:
    """Модель для анализа договоров и извлечения ключевых данных."""

    def __init__(self):
        self.ai = AIService()

    def analyze_contract(self, file_content: bytes) -> Dict[str, Any]:
        """
        Анализирует загруженный договор и извлекает структурированные данные.

        Args:
            file_content (bytes): Бинарное содержимое файла договора.

        Returns:
            dict: Структурированные данные договора.
        """
        # Заглушка для примера (реализуйте парсинг PDF/DOCX через pdfminer/docx2txt)
        text_content = "Предмет договора: поставка оборудования. Срок: 12 месяцев."

        return {
            "subject": self._extract_subject(text_content),
            "parties": self._identify_parties(text_content),
            "terms": self._extract_terms(text_content)
        }

    def _extract_subject(self, text: str) -> str:
        """Извлекает предмет договора через ИИ."""
        return self.ai.query(f"Извлеки предмет договора из текста: {text[:1000]}")

    def _identify_parties(self, text: str) -> list:
        """Идентифицирует стороны договора."""
        return self.ai.query(f"Найди стороны договора в тексте: {text[:1000]}")

    def _extract_terms(self, text: str) -> dict:
        """Извлекает существенные условия."""
        return self.ai.query(f"Выдели сроки, бюджет и этапы из: {text[:1000]}")