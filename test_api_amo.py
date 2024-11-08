import os
import requests
from datetime import datetime
from pprint import pprint

from dotenv import load_dotenv

from constans import STATUSES_LEADS, ID_VOR

load_dotenv()

data = [
    {
        "airtable_id": "M13752",
        "amount_paid": 7000,
        "course_code": "ISB_7.7.07",
        "date_received": "2021-10-01",
        "price": 7000,
        "student_email": "uuu@gmail.com",
        "student_name": "Name1",
        "student_phone": "+770000000000",
        "student_surname": "Surname1",
        "submission_id": "P18814",
        "status": "Оплачена полностью",
    },
    # {
    #     "airtable_id": "M13753",
    #     "amount_paid": 472,
    #     "course_code": "ISB_7.7.07",
    #     "date_received": "2021-10-01",
    #     "price": 472,
    #     "student_email": "nnn@yandex.ru",
    #     "student_name": "Name2",
    #     "student_phone": "+770000000001",
    #     "student_surname": "Surname2",
    #     "submission_id": "P18815",
    #     "status": "Оплачена полностью"
    # },
]


def date_str_to_unix(date_str: str):
    """Преобразование строки в unixtime."""
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())


def create_list_leads(data_json: list[dict]):
    """Создание списка сделок для отправки в amoCRM."""
    leads = list()
    for lead_data in data_json:
        lead = dict(
            name=str(
                lead_data.get("airtable_id")
                + " "
                + lead_data.get("course_code")
            ),
            price=int(lead_data.get("price")),
            status_id=STATUSES_LEADS[lead_data.get("status")],
            pipeline_id=ID_VOR,
            created_at=date_str_to_unix(lead_data.get("date_received")),
            created_by=0,
            _embedded=dict(
                contacts=[
                    dict(
                        first_name=lead_data.get("student_name"),
                        last_name=lead_data.get("student_surname"),
                        name=str(
                            lead_data.get("student_name")
                            + " "
                            + lead_data.get("student_surname")
                        ),
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


def get_lead(id: str):
    """Получение сделки по ID."""
    api_answer = requests.get(
        "https://softculture.amocrm.ru/api/v4/leads/{}".format(id),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )
    print(api_answer.status_code)
    pprint(api_answer.json())


def get_contact(id: str):
    """Получение контакта по ID."""
    api_answer = requests.get(
        "https://softculture.amocrm.ru/api/v4/contacts/{}".format(id),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )
    print(api_answer.status_code)
    pprint(api_answer.json())


def post_leads(data_json: list):
    """Создание сделок в amoCRM."""
    api_answer = requests.post(
        "https://softculture.amocrm.ru/api/v4/leads/complex",
        headers={
            "Authorization": f"Bearer {os.getenv('TOKEN_AMO')}",
            "Content-Type": "application/json",
        },
        json=create_list_leads(data_json),
    )
    print(api_answer.status_code)
    pprint(api_answer.json())


get_lead("13282723")
# get_contact("16823473")
# create_list_leads(data)
# post_leads(data)
