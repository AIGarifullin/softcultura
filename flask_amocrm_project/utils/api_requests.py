"""Модуль заросов API проекта."""

import http
import logging
import os

import requests

from dotenv import load_dotenv

from .utils import create_list_leads, try_except_decorator
from ..config import GET_LEAD, GET_LEADS_LIST, POST_LEADS

logger = logging.getLogger("Flask_App")

load_dotenv()


@try_except_decorator
def get_leads_list():
    """Получение списка сделок."""
    response = requests.get(
        GET_LEADS_LIST,
        headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
        params=dict(limit=2),
        timeout=10,  # Устанавливаем тайм-аут в 10 секунд
    )
    if response.status_code != http.HTTPStatus.OK:
        logger.error(f"Response status code: {response.status_code}")
        return {"error": "Authorization Error"}, response.status_code
    logger.info(f"Response status code: {response.status_code}")
    return response.json(), response.status_code


@try_except_decorator
def get_lead(id):
    """Получение сделки по ID."""
    response = requests.get(
        GET_LEAD.format(int(id)),
        headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
        timeout=10,
    )
    if response.status_code != http.HTTPStatus.OK:
        logger.error(f"Response status code: {response.status_code}")
        return {"error": "Lead not found"}, response.status_code
    logger.info(f"Response status code: {response.status_code}")
    return response.json(), response.status_code


@try_except_decorator
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
