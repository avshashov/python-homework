import requests
import time
from datetime import datetime, timedelta


def all_questions(days_ago=2):
    todate = int(datetime.timestamp((datetime.today())))
    fromdate = int(datetime.timestamp((datetime.today() - timedelta(days=days_ago))))

    url = 'https://api.stackexchange.com/2.3/questions'

    page_number, question_number = 1, 1
    while True:
        params = {
            'page': page_number, 'pagesize': 100, 'fromdate': fromdate,
            'todate': todate,
            'order': 'desc', 'sort': 'creation',
            'tagged': 'python', 'site': 'stackoverflow'
        }

        response = requests.get(url=url, params=params)

        if response.status_code >= 400:
            print(f'Error: {response.status_code}')
            break

        time.sleep(2)
        questions = response.json()

        for key, value in questions.items():
            if key == 'items':
                if len(value) > 0:
                    for n, question in enumerate(value, question_number):
                        dt = (datetime.fromtimestamp(question['creation_date']))
                        print(f'{n}. Question: {question["title"]} \nCreation date: {dt}\n')
                        question_number += 1
                else:
                    return None
        page_number += 1


all_questions()
