"""Модуль заросов API проекта."""

import http
import logging
import os
import requests

from .utils import create_list_leads, request_error_decor
from ..config import GET_LEAD, GET_LEADS_LIST, POST_LEADS

logger = logging.getLogger("Flask_App")


@request_error_decor
def get_lead(id: int):
    """Получение сделки по ID."""
    api_answer = requests.get(
        GET_LEAD.format(id),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )
    if api_answer.status_code != http.HTTPStatus.OK:
        logger.error(f"Статус код ответа: {api_answer.status_code}")
        return dict(error="Lead not found"), api_answer.status_code
    logger.info(f"Код ответа {api_answer.status_code}")
    return api_answer.json(), api_answer.status_code


@request_error_decor
def get_leads_list():
    """Получение списка сделок."""
    response = requests.get(
        GET_LEADS_LIST,
        headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
        timeout=10,  # Устанавливаем тайм-аут в 10 секунд
    )
    if response.status_code != http.HTTPStatus.OK:
        logger.error(f"Response status code: {response.status_code}")
        return {"error": "Authorization Error"}, response.status_code
    logger.info(f"Response status code: {response.status_code}")
    return response.json(), response.status_code


@request_error_decor
def post_leads(data_json: list[dict]):
    """Создание сделок в amoCRM."""
    response = requests.post(
        POST_LEADS,
        headers={
            "Authorization": f"Bearer {os.getenv('TOKEN_AMO')}",
            "Content-Type": "application/json",
        },
        json=create_list_leads(data_json),
        timeout=10,
    )
    if response.status_code != http.HTTPStatus.OK:
        logger.error(f"Response status code: {response.status_code}")
        return {"error": "Request error"}, response.status_code
    logger.info(f"Response status code: {response.status_code}")
    return response.json(), response.status_code
