"""Модуль настроек и констант проекта"""

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


data = [
    {
        "airtable_id": "M13752",
        "amount_paid": 7000,
        "course_code": "ISB_7.7.07",
        "date_received": "2021-10-01",
        "price": 7000,
        "student_email": "uuu@gmail.com",
        "student_name": "Name1",
        "student_phone": "+770000000000",
        "student_surname": "Surname1",
        "submission_id": "P18814",
        "status": "Оплачена полностью",
    },
]

# # Глобальные настройки логгера
BACKUP_COUNT = 5
ENCODING = "UTF-8"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOGGING_LEVEL = "DEBUG"
LOGS_FOLDER = "logs"
LOGS_FILE = "logfile.log"
MAX_BYTES = 50_000_000