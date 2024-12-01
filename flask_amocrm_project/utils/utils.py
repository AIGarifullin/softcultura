"""Модуль утилит проекта."""

import http
import json
import logging
from datetime import datetime

from requests.exceptions import RequestException

from ..config import STATUSES_LEADS, ID_VOR

logger = logging.getLogger("Flask_App")


def request_error_decor(func):
    """
    Декоратор перехвата ошибок обращения по URLs к API сервисов заказчика.
    """

    def wapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except json.JSONDecodeError as error:
            logger.error("Ошибка декодирования JSON.")
            return (
                dict(error=f"Ошибка декодирования JSON: {error}"),
                http.HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        except RequestException as error:
            logger.error("Ошибка запроса к URL.")
            return (
                dict(error=f"Request Error: {error}"),
                http.HTTPStatus.BAD_REQUEST,
            )

    return wapper


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
