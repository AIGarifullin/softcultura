"""Модуль представлений API проекта"""

from flask import jsonify, request

from . import app
from .utils.api_requests import get_lead, get_leads_list, post_leads


@app.route("/api/v1/leads/<int:id>", methods=("GET",))
def lead_by_id(id: int):
    """Маршрут для получения сделки по ID."""
    response_data, status_code = get_lead(id)
    return jsonify(response_data), status_code


@app.route("/api/v1/leads/", methods=("GET", "POST"))
def get_leads_list_and_post_leads_route():
    """Маршрут для получения списка сделок и их создания."""
    if request.method == "GET":
        response_data, status_code = get_leads_list()
    elif request.method == "POST":
        response_data, status_code = post_leads(request.get_json())
    return jsonify(response_data), status_code
