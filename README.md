# Telegram-бот для анализа договоров и закупок (ProTalk)

## 🚀 **Быстрый старт**
1. **Клонируйте репозиторий**:
```bash
cd /home/aa_lozovoy/PythonProject/
git clone https://github.com/yourusername/project.git "Tg-bot ProTalk"
cd "Tg-bot ProTalk"
```

2. **Установите зависимости**:
```bash
pip install -r requirements.txt
```

3. **Создайте бота в Telegram** через [@BotFather](https://t.me/BotFather) и добавьте токен в `.env`:
```ini
BOT_TOKEN=ваш_токен_бота
```

4. **Заполните `.env`** (на основе `.env.example`):
```ini
OPENAI_API_KEY=sk-ваш_ключ
PROCUREMENT_API_KEY=ваш_ключ
PROCUREMENT_API_URL=https://api.procurement.ru
GOOGLE_SHEETS_ID=ваш_id
GOOGLE_CREDENTIALS_JSON='{"type": "service_account", ...}'
ADMIN_CHAT_ID=ваш_chat_id
```

5. **Запустите бота**:
```bash
python main.py
```

---

## 📌 **Функционал**
- **Кнопка 1**: Анализ договоров через GPT-4. Отправьте файл → получите рекомендации в DOCX.
- **Кнопка 2**: Поиск закупок по API. Введите запрос (например, `Станки, 28.91`) → получите Excel-отчет.

---

## 🔧 **Интеграция с API**
### Для кнопки 2 (пример кода):
```python
# models/procurement_api.py
import requests
from config.settings import Config

def fetch_procurements(product: str):
    response = requests.get(
        f"{Config.PROCUREMENT_API_URL}/search",
        headers={"Authorization": f"Bearer {Config.PROCUREMENT_API_KEY}"},
        params={"product": product}
    )
    return response.json()
```

---

## 📊 **Google Sheets как БД**
1. Создайте таблицу и настройте доступ ([инструкция](https://vc.ru/ai/1455895)).
2. Пример сохранения данных:
```python
# models/google_sheets_db.py
from models.google_sheets_db import GoogleSheetsDB
db = GoogleSheetsDB()
db.save_data({"Товар": "Станки", "КВЭД": "28.91", "Статус": "Активна"})
```

---

## 🔒 **Безопасность**
- Не публикуйте `.env`! ([гайд](https://habr.com/ru/articles/820461/)).
- Логирование:
```python
# config/logger_config.py
import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)
```

---

## 📞 **Поддержка**
- **Ошибки**: [Создать issue](https://github.com/yourusername/project/issues).
- **Чат**: [Telegram](https://t.me/your_channel).
- **Статьи**: 
  - [ИИ для анализа договоров](https://habr.com/ru/articles/861770/).
  - [Парсинг закупок](https://habr.com/ru/articles/785888/).

---

## 📄 **Лицензия**
MIT License. Подробнее в [LICENSE](LICENSE).