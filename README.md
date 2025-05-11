# 🤖 ProTalk Chat Bot – Юридический ассистент

![Architecture](https://img.shields.io/badge/Architecture-MVC-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-API%20v20.0-blue)

Telegram-бот для автоматизации юридических задач, включая генерацию договоров, мониторинг закупок и интеграцию с платформой ProTalk и внешними API.

---

📌 Возможности

- 📄 Составление договоров на основе юридических прецедентов  
- 🛒 Мониторинг активных закупок по ключевым словам  
- 🔗 Интеграция с ProTalk API  
- 🧠 Генерация текста с помощью OpenAI API  
- 🔍 Расширяемая архитектура (MVC)

---

⚙️ Требования

- Python 3.10+
- PostgreSQL 14+ (рекомендуется)
- Аккаунт Telegram
- Доступ к ProTalk Developer Portal и OpenAI API

---

🚀 Установка и запуск

1. Клонируйте репозиторий

git clone https://github.com/yourusername/protalk-bot.git
cd protalk-bot


2. Создайте виртуальное окружение и установите зависимости

python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
pip install -r requirements.txt


3. Создайте Telegram-бота

Найдите @BotFather
Отправьте команду /newbot
Укажите имя и username (например: LegalAssistantBot_bot)
Скопируйте полученный токен и сохраните


4. Получите ключи ProTalk API

Перейдите в ProTalk Developer Portal
Создайте приложение
Получите API_KEY и SECRET_TOKEN


5. Настройте переменные окружения
Создайте файл .env в корне проекта или скопируйте из шаблона:
cp .env.example .env

Пример содержимого .env:
BOT_TOKEN=ваш_telegram_token
PROTALK_API_KEY=ваш_protalk_api_key
PROTALK_SECRET=ваш_protalk_secret
OPENAI_API_KEY=sk-ваш_openai_api_key
DB_URL=postgresql://user:password@localhost:5432/legalbot

6. Запуск бота
🔧 Режим разработки

gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

💬 Команды Telegram-бота

| Команда        | Описание                                    |
| -------------- | ------------------------------------------- |
| `/start`       | Приветствие и краткое описание возможностей |
| `/contract`    | Загрузка договора для анализа (PDF/DOCX)    |
| `/procurement` | Мониторинг закупок по ключевым словам       |


🛠 Планы по доработке (roadmap)

✅ Интеграция с ProTalk API
🔜 Интеграция с ЕИС и СберАСТ
🔜 Webhook-режим вместо polling
🔜 Асинхронные задачи через Celery
🔜 Веб-панель администратора
🔜 Покрытие unit-тестами


♻️ Обновление проекта

git pull origin main
pip install -r requirements.txt


⚠️ Важные примечания

Используйте HTTPS в production
Проверьте переменные окружения перед запуском
Добавьте .env в .gitignore

