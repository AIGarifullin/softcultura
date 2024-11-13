import os
import requests

from dotenv import load_dotenv
from flask import Flask, jsonify

from flask_amocrm_project.utils.utils import (create_list_leads,
                                              is_list_of_dicts)

load_dotenv()

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=os.getenv('DEBUG', 'False') == 'True'
))


def get_leads_list():
    """Получение списка сделок."""
    api_answer = requests.get(
        "https://softculture.amocrm.ru/api/v4/leads",
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )

    if api_answer.status_code == 200:
        return api_answer.json()
    else:
        return {'error': 'Authorization error'}, api_answer.status_code


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

@app.route('/leads')
def get_leads_list_route():
    """Маршрут для получения списка сделок."""
    leads_list_data = get_leads_list()
    return jsonify(leads_list_data)


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
