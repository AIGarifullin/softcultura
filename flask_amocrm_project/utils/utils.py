import logging

import requests

from datetime import datetime

from flask import jsonify

from flask_amocrm_project.config import STATUSES_LEADS, ID_VOR

logger = logging.getLogger("API")


def date_str_to_unix(date_str: str):
    """Преобразование строки в unixtime."""
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())


def create_list_leads(data_json: list[dict]):
    """Создание списка сделок для отправки в amoCRM."""
    leads = list()
    for lead_data in data_json:
        lead = dict(
            id=str(lead_data.get("submission_id")),
            name=str(
                f'{lead_data.get("airtable_id")} '
                f'{lead_data.get("course_code")}'
            ),
            price=int(lead_data.get("price")),
            status_id=STATUSES_LEADS[lead_data.get("status")],
            pipeline_id=ID_VOR,
            created_at=date_str_to_unix(lead_data.get("date_received")),
            created_by=0,
            score=(
                int(lead_data.get("amount_paid"))
                if lead_data.get("amount_paid") is not None
                else None
            ),
            _embedded=dict(
                contacts=[
                    dict(
                        first_name=lead_data.get("student_name"),
                        last_name=lead_data.get("student_surname"),
                        name=str(
                            f'{lead_data.get("student_name")} '
                            f'{lead_data.get("student_surname")}'
                        ),
                        student_id=str(lead_data.get("student_id")),
                        custom_fields_values=[
                            dict(
                                field_code="PHONE",
                                values=[
                                    dict(
                                        enum_code="WORK",
                                        value=lead_data.get("student_phone"),
                                    ),
                                ],
                            ),
                            dict(
                                field_code="EMAIL",
                                values=[
                                    dict(
                                        enum_code="WORK",
                                        value=lead_data.get("student_email"),
                                    )
                                ],
                            ),
                        ],
                    )
                ]
            ),
        )
        leads.append(lead)
    return leads


def error_handling(response, err):
    """Обрабатывает исключения запросов и возвращает соответствующий ответ."""
    if isinstance(err, requests.exceptions.HTTPError):
        logger.error(f"HTTP Error: {err}, Код ответа: {response.status_code}")
        return (
            jsonify({"error": "HTTP Error", "message": str(err)}),
            response.status_code,
        )
    elif isinstance(err, requests.exceptions.ConnectionError):
        logger.error(
            f"Connection Error: {err}, Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Connection Error", "message": str(err)}),
            502,
        )
    elif isinstance(err, requests.exceptions.Timeout):
        logger.error(
            f"Timeout Error: {err}, Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Timeout Error", "message": str(err)}),
            504,
        )
    else:
        logger.error(
            f"Request Error: {err}, Код ответа: {response.status_code}"
        )
        return (
            jsonify({"error": "Request Error", "message": str(err)}),
            500,
        )
