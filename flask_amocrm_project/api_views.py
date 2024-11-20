"""Модуль API проекта"""
import logging
import os

import requests

from dotenv import load_dotenv
from flask import jsonify

from .config import data, GET_LEAD, GET_LEADS_LIST, POST_LEADS
from .main import app
from .utils.utils import create_list_leads


logger = logging.getLogger("API")

load_dotenv()


@app.route("/api/v1/leads/", methods=("GET",))
def get_leads_list():
    """Маршрут для получения списка сделок."""
    try:
        response = requests.get(
            GET_LEADS_LIST,
            headers={"Authorization": f"Bearer {os.getenv('TOKEN_AMO')}"},
            timeout=10,  # Устанавливаем тайм-аут в 10 секунд
        )
        response.raise_for_status()  # Проверяем на наличие HTTP ошибок
        logger.info(f"Код ответа {response.status_code}")
        return jsonify(response.json())
    except requests.exceptions.HTTPError as http_err:
        logger.error(
            f"HTTP Error: {http_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "HTTP Error", "message": str(http_err)}),
            response.status_code,
        )
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(
            f"Connection Error: {conn_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Connection Error", "message": str(conn_err)}),
            502,
        )
    except requests.exceptions.Timeout as timeout_err:
        logger.error(
            f"Timeout Error: {timeout_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Timeout Error", "message": str(timeout_err)}),
            504,
        )
    except requests.exceptions.RequestException as req_err:
        logger.error(
            f"Request Error: {req_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Request Error", "message": str(req_err)}),
            500,
        )


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
    except requests.exceptions.HTTPError as http_err:
        logger.error(
            f"HTTP Error: {http_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "HTTP Error", "message": str(http_err)}),
            response.status_code,
        )
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(
            f"Connection Error: {conn_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Connection Error", "message": str(conn_err)}),
            502,
        )
    except requests.exceptions.Timeout as timeout_err:
        logger.error(
            f"Timeout Error: {timeout_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Timeout Error", "message": str(timeout_err)}),
            504,
        )
    except requests.exceptions.RequestException as req_err:
        logger.error(
            f"Request Error: {req_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Request Error", "message": str(req_err)}),
            500,
        )


@app.route("/api/v1/leads/complex")
def post_leads():
    """Маршрут для создания сделок."""
    try:
        response = requests.post(
            POST_LEADS,
            headers={
                "Authorization": f"Bearer {os.getenv('TOKEN_AMO')}",
                "Content-Type": "application/json",
            },
            json=create_list_leads(data),
            timeout=10,
        )
        response.raise_for_status()
        logger.info(f"Код ответа {response.status_code}")
        return jsonify(response.json())
    except requests.exceptions.HTTPError as http_err:
        logger.error(
            f"HTTP Error: {http_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "HTTP Error", "message": str(http_err)}),
            response.status_code,
        )
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(
            f"Connection Error: {conn_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Connection Error", "message": str(conn_err)}),
            502,
        )
    except requests.exceptions.Timeout as timeout_err:
        logger.error(
            f"Timeout Error: {timeout_err}, "
            f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Timeout Error", "message": str(timeout_err)}),
            504,
        )
    except requests.exceptions.RequestException as req_err:
        logger.error(
            f"Request Error: {req_err}, " f"Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Request Error", "message": str(req_err)}),
            500,
        )
