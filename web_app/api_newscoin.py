import sqlite3
import time

import pytz
from dateutil import parser
from newsapi import NewsApiClient

check_period = 300


def main():
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    api = NewsApiClient(api_key='13df53b7cecf4d1e9efc7a312afa65a7')

    response = api.get_everything(q='coin', language='ru',)
    data = response['articles']
    cursor.execute('DELETE FROM api_news;')
    for value in data:
        timestamp = value['publishedAt']
        timestamp_local = parser.parse(
            timestamp
            ).astimezone(pytz.timezone('Turkey'))
        formatted_timestamp = timestamp_local.strftime('%Y-%m-%d')
        news_list = []
        news_list.append(str(value['author']))
        news_list.append(str(value['description']))
        news_list.append(str(value['title']))
        news_list.append(str(formatted_timestamp))
        fields = '(author, description, title, published)'
        news_list = tuple(news_list)
        insert_records = f"""INSERT INTO api_news {fields} VALUES {news_list};"""
        cursor.execute(insert_records)

    connection.commit()

    connection.close()


while True:
    main()
    time.sleep(check_period)
