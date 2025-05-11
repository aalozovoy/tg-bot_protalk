from typing import Dict, Any
from pdfminer.high_level import extract_text
from docx import Document
import io
import logging
from app.services.ai_service import AIService


class ContractModel:
    """Модель для анализа договоров и извлечения ключевых данных."""

    def __init__(self):
        self.ai = AIService()
        self.logger = logging.getLogger(__name__)

    def analyze_contract(self, file_content: bytes) -> Dict[str, Any]:
        """
        Анализирует загруженный договор и извлекает структурированные данные.

        Args:
            file_content (bytes): Бинарное содержимое файла договора.

        Returns:
            dict: Структурированные данные договора или пустой словарь при ошибке.
        """
        try:
            text_content = self._parse_file_content(file_content)
            if not text_content:
                return {}

            return {
                "subject": self._extract_subject(text_content),
                "parties": self._identify_parties(text_content),
                "terms": self._extract_terms(text_content)
            }

        except Exception as e:
            self.logger.error(f"Ошибка анализа договора: {str(e)}")
            return {}

    def _parse_file_content(self, file_content: bytes) -> str:
        """Парсит содержимое файла в текст."""
        try:
            # Определение формата файла по сигнатуре
            if file_content.startswith(b'%PDF'):
                return self._parse_pdf(file_content)
            elif file_content.startswith(b'PK\x03\x04'):
                return self._parse_docx(file_content)
            else:
                raise ValueError("Неподдерживаемый формат файла")

        except Exception as e:
            self.logger.error(f"Ошибка парсинга файла: {str(e)}")
            return ""

    def _parse_pdf(self, content: bytes) -> str:
        """Парсит PDF-документ."""
        try:
            with io.BytesIO(content) as pdf_file:
                return extract_text(pdf_file)
        except Exception as e:
            self.logger.error(f"Ошибка парсинга PDF: {str(e)}")
            return ""

    def _parse_docx(self, content: bytes) -> str:
        """Парсит DOCX-документ."""
        try:
            with io.BytesIO(content) as docx_file:
                doc = Document(docx_file)
                return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            self.logger.error(f"Ошибка парсинга DOCX: {str(e)}")
            return ""

    def _extract_subject(self, text: str) -> str:
        """Извлекает предмет договора через ИИ."""
        return self.ai.generate_contract_clauses(
            f"Извлеки предмет договора из текста: {text[:2000]}"
        )

    def _identify_parties(self, text: str) -> list:
        """Идентифицирует стороны договора."""
        return self.ai.generate_contract_clauses(
            f"Найди стороны договора в тексте: {text[:2000]}"
        )

    def _extract_terms(self, text: str) -> dict:
        """Извлекает существенные условия."""
        return self.ai.generate_contract_clauses(
            f"Выдели сроки, бюджет и этапы из: {text[:2000]}"
        )