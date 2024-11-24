"""Модуль утилит проекта."""

import http
import json
import logging
import os
import requests
from requests.exceptions import RequestException

from ..config import GET_LEAD

logger = logging.getLogger("Flask_App")


def get_lead(id: int):
    """Получение сделки по ID."""
    try:
        api_answer = requests.get(
            GET_LEAD.format(id),
            headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
        )
        if api_answer.status_code != http.HTTPStatus.OK:
            logger.error(f"Статус код ответа: {api_answer.status_code}")
            return dict(error="Lead not found"), api_answer.status_code
        logger.info(f"Код ответа {api_answer.status_code}")
        return api_answer.json(), api_answer.status_code
    except json.JSONDecodeError as error:
        logger.error("Ошибка декодирования JSON.")
        return (
            dict(error=f"Ошибка декодирования JSON: {error}"),
            api_answer.status_code,
        )
    except RequestException as error:
        logger.error("Ошибка запроса к URL.")
        return dict(error=f"Request Error: {error}"), api_answer.status_code
