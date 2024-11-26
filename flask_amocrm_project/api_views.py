"""Модуль API проекта"""
import logging
import os

import requests

from dotenv import load_dotenv
from flask import request, jsonify

from .config import GET_LEAD, GET_LEADS_LIST, POST_LEADS
from .main import app
from .utils.utils import create_list_leads, error_handling


logger = logging.getLogger("API")

load_dotenv()


@app.route("/api/v1/leads/", methods=("GET", "POST"))
def get_leads_list_and_post_leads():
    """Маршрут для получения списка сделок и их создания."""
    if request.method == "GET":
        try:
            response = requests.get(
                GET_LEADS_LIST,
                headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
                timeout=10,  # Устанавливаем тайм-аут в 10 секунд
            )
            response.raise_for_status()  # Проверяем на наличие HTTP ошибок
            logger.info(f"Код ответа {response.status_code}")
            return jsonify(response.json())
        except requests.exceptions.RequestException as err:
            return error_handling(response, err)
    elif request.method == "POST":
        try:
            response = requests.post(
                POST_LEADS,
                headers={
                    "Authorization": f"Bearer {os.getenv('TOKEN_AMO')}",
                    "Content-Type": "application/json",
                },
                json=create_list_leads(data),  # noqa
                timeout=10,
            )
            response.raise_for_status()
            logger.info(f"Код ответа {response.status_code}")
            return jsonify(response.json())
        except requests.exceptions.RequestException as err:
            return error_handling(response, err)


@app.route("/api/v1/leads/<int:id>", methods=("GET",))
def get_lead(id: int):
    """Маршрут для получения сделки по ID."""
    try:
        response = requests.get(
            GET_LEAD.format(id),
            headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
            timeout=10,
        )
        response.raise_for_status()
        logger.info(f"Код ответа {response.status_code}")
        return jsonify(response.json())
    except requests.exceptions.RequestException as err:
        return error_handling(response, err)
