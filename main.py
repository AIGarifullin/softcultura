import os
import requests

from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify

from config import data, STATUSES_LEADS, ID_VOR

load_dotenv()

app = Flask(__name__)
app.config.from_object(__name__)

# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
    DEBUG=os.getenv('DEBUG', 'False') == 'True'
))


def date_str_to_unix(date_str: str):
    """Преобразование строки в unixtime."""
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())


def is_list_of_dicts(data):
    """Проверка типа data на list[dict]"""
    if isinstance(data, list):
        return all(isinstance(item, dict) for item in data)
    return False


def create_list_leads(data_json: list[dict]):
    """Создание списка сделок для отправки в amoCRM."""
    leads = list()
    for lead_data in data_json:
        lead = dict(
            name=str(
                lead_data.get("airtable_id")
                + " "
                + lead_data.get("course_code")
            ),
            price=int(lead_data.get("price")),
            status_id=STATUSES_LEADS[lead_data.get("status")],
            pipeline_id=ID_VOR,
            created_at=date_str_to_unix(lead_data.get("date_received")),
            created_by=0,
            _embedded=dict(
                contacts=[
                    dict(
                        first_name=lead_data.get("student_name"),
                        last_name=lead_data.get("student_surname"),
                        name=str(
                            lead_data.get("student_name")
                            + " "
                            + lead_data.get("student_surname")
                        ),
                        custom_fields_values=[
                            dict(
                                field_code="PHONE",
                                values=[
                                    dict(
                                        enum_code="WORK",
                                        value=lead_data.get("student_phone"),
                                    ),
                                ],
                            ),
                            dict(
                                field_code="EMAIL",
                                values=[
                                    dict(
                                        enum_code="WORK",
                                        value=lead_data.get("student_email"),
                                    )
                                ],
                            ),
                        ],
                    )
                ]
            ),
        )
        leads.append(lead)
    return leads


def get_lead(id: int):
    """Получение сделки по ID."""
    api_answer = requests.get(
        "https://softculture.amocrm.ru/api/v4/leads/{}".format(id),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )

    if api_answer.status_code == 200:
        return api_answer.json()
    else:
        return {'error': 'Lead not found'}, api_answer.status_code


def post_leads(data_json: list[dict]):
    """Создание сделок в amoCRM."""
    api_answer = requests.post(
        "https://softculture.amocrm.ru/api/v4/leads/complex",
        headers={
            "Authorization": f"Bearer {os.getenv('TOKEN_AMO')}",
            "Content-Type": "application/json",
        },
        json=create_list_leads(data_json),
    )

    return api_answer.json(), api_answer.status_code


@app.route('/leads/<int:id>')
def get_lead_route(id):
    """Маршрут для получения сделки по ID."""
    lead_data = get_lead(id)
    return jsonify(lead_data)


@app.route('/leads/complex')
def post_leads_route():
    """Маршрут для создания сделок."""
    if is_list_of_dicts(data):
        response_data, status_code = post_leads(data)
        return jsonify(response_data), status_code
    else:
        return jsonify({'error': 'Check data'}), 400


if __name__ == '__main__':
    app.run()
