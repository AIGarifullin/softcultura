"""Модуль заросов API проекта."""

import http
import logging
import os
import requests

from .utils import request_error_decor
from ..config import GET_LEAD

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
