"""Модуль утилит проекта."""

import os
import requests

from dotenv import load_dotenv

from ..config import GET_LEAD

load_dotenv()


def get_lead(id: int):
    """Получение сделки по ID."""
    api_answer = requests.get(
        GET_LEAD.format(id),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )

    if api_answer.status_code == 200:
        return api_answer.json(), api_answer.status_code
    else:
        return dict(error="Lead not found"), api_answer.status_code
