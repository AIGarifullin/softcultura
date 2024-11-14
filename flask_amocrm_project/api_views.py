"""Модуль API проекта"""

import logging
from flask import jsonify

from . import app
from .utils.utils import get_lead

logger = logging.getLogger("API")


@app.route("/api/v1/leads/<int:id>", methods=("GET",))
def lead_by_id(id: int):
    """Маршрут для получения сделки по ID."""
    response_data, status_code = get_lead(id)
    logger.info(f"Код ответа {status_code}")
    return jsonify(response_data), status_code
