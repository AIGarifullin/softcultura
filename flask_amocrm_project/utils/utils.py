"""Модуль утилит проекта."""

import http
import json
import os
import requests
from requests.exceptions import RequestException

from ..config import GET_LEAD


def get_lead(id: int):
    """Получение сделки по ID."""
    try:
        api_answer = requests.get(
            GET_LEAD.format(id),
            headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
        )
        if api_answer.status_code != http.HTTPStatus.OK:
            return dict(error="Lead not found"), api_answer.status_code
        return api_answer.json(), api_answer.status_code
    except json.JSONDecodeError as error:
        return (
            dict(error=f"Ошибка декодирования JSON: {error}"),
            api_answer.status_code,
        )
    except RequestException as error:
        return dict(error=f"Request Error: {error}"), api_answer.status_code
