import requests
from datetime import datetime, timedelta


def all_questions(days_ago=2):
    todate = int(datetime.timestamp((datetime.today())))
    fromdate = int(datetime.timestamp((datetime.today() - timedelta(days=days_ago))))

    url = 'https://api.stackexchange.com/2.3/questions'

    params = {
        'pagesize': 50, 'fromdate': fromdate, 'todate': todate,
        'order': 'desc', 'sort': 'creation',
        'tagged': 'python', 'site': 'stackoverflow'
    }
    responce = requests.get(url=url, params=params)
    stack_dict = responce.json()
    for key, value in stack_dict.items():
        if key == 'items':
            for n, question in enumerate(value, 1):
                dt = (datetime.fromtimestamp(question['creation_date']))
                print(f'{n}. Question: {question["title"]} \nCreation date: {dt}\n')


all_questions()
