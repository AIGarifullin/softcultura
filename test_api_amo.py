import os
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

url = "https://softculture.amocrm.ru/api/v4/leads/11677397"

api_answer = requests.get(
        url,
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )

print(api_answer.status_code)
pprint(api_answer.json())
