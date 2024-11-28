"""Модуль представлений API проекта"""

from flask import jsonify

from . import app
from .utils.api_requests import get_lead


@app.route("/api/v1/leads/<int:id>", methods=("GET",))
def lead_by_id(id: int):
    """Маршрут для получения сделки по ID."""
    response_data, status_code = get_lead(id)
    return jsonify(response_data), status_code
