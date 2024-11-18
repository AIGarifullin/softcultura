# Конфигурация и константы проекта

# Отношение состояний сделки
STATUSES_LEADS = {
    "Нет оплаты": 66431750,
    "Оплачена полностью": 142,
    "Оплачена частично": 142,
    "Оплачена с переплатой": 142,
    "Отменена": 143,
}

# ID воронки "Воронка" в проекте amoCRM
ID_VOR = 8117898

# # Глобальные настройки логгера
BACKUP_COUNT = 5
ENCODING = "UTF-8"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOGGING_LEVEL = "DEBUG"
LOGS_FOLDER = "logs"
LOGS_FILE = "logfile.log"
MAX_BYTES = 50_000_000
