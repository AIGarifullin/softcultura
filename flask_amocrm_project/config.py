"""Модуль настроек и констант проекта"""

import os
from datetime import timedelta


# # Config Flask
class Config(object):
    """Кофиг фласк."""

    # Не переопределяем словарь, а сразу формируем с нужными значениями
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SECRET_KEY = os.getenv("SECRET_KEY", default="default")


# # Глобальные настройки логгера
BACKUP_COUNT = 5
ENCODING = "UTF-8"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOGGING_LEVEL = "DEBUG"
LOGS_FOLDER = "logs"
LOGS_FILE = "logfile.log"
MAX_BYTES = 50_000_000

# # URL's amoCRM
GET_LEAD = "https://softculture.amocrm.ru/api/v4/leads/{}"
