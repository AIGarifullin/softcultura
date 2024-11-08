import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

url = "https://softculture.amocrm.ru/api/v4/leads/{}"

api_answer = requests.get(
        url.format("13189813"),
        headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    )

print(api_answer.status_code)
print(api_answer.json())

obj =   [{'name':'M13752-ISB_7.7.07','price':7000,'status_id':66431750}]


api_post = requests.post(
    url='https://softculture.amocrm.ru/api/v4/leads',
    headers=dict(Authorization=f"Bearer {os.getenv('TOKEN_AMO')}"),
    data=json.dumps(obj),
)

print(api_post.status_code)
print(api_post.json())
