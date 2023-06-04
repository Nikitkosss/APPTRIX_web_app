import configparser
import json
import sqlite3

import pytz
from dateutil import parser
from requests import Session

config = configparser.ConfigParser()
config.read('coinmarket.ini')
headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '8fcea442-9d72-4c4a-9261-39d2191848c9'
    }
connection = sqlite3.connect('web_app/db.sqlite3')
cursor = connection.cursor()


def coins_list():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    info = json.loads(response.text)
    coin_list = []
    for coin in info['data']:
        coin_list.append(coin['name'])
    return coin_list


def get_info():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    coin_list = coins_list()
    ten_coin = coin_list[:10]
    for coin in ten_coin:
        coins = []
        parameters = {'slug': coin.lower(), 'convert': 'USD'}
        session = Session()
        session.headers.update(headers)
        response = session.get(url, params=parameters)
        info = json.loads(response.text)
        data = info['data']
        timestamp = info['status']['timestamp']
        timestamp_local = parser.parse(
            timestamp
            ).astimezone(pytz.timezone('Turkey'))
        formatted_timestamp = timestamp_local.strftime('%Y-%m-%d')
        for value in data.values():
            coins.append(value['symbol'])
            coins.append(value['name'])
            coins.append(value['quote']['USD']['price'])
            coins.append(value['total_supply'])
            coins.append(value['quote']['USD']['percent_change_24h'])
            coins.append(formatted_timestamp)
            fields = '(code,name,price,total_supply, percent_change,timestamp)'
            coins = tuple(coins)
            insert_records = f"""INSERT INTO
            api_coin {fields} VALUES {coins};"""
            cursor.execute(insert_records)
    connection.commit()
    connection.close()


get_info()
