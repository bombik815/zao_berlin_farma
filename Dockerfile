FROM python:3.12-slim

WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходных файлов проекта
COPY . .

# Переменные окружения по умолчанию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]