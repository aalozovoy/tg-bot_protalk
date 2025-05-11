import openai
from app import Config


class AIService:
    """Сервис для взаимодействия с OpenAI API."""

    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY

    def generate_contract_clauses(self, context: str) -> str:
        """
        Генерирует блоки договора на основе прецедентов через ChatGPT.

        Args:
            context (str): Контекст для анализа (текст договора или описание условий).

        Returns:
            str: Сгенерированные рекомендации.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты юрист-ассистент. Сгенерируй блоки договора."},
                {"role": "user", "content": context}
            ]
        )
        return response.choices[0].message.content