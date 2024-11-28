"""Модуль утилит проекта."""

import http
import json
import logging
from requests.exceptions import RequestException

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
