from http import HTTPStatus

import pytest

from tests.utils import check_permissions, create_coins


@pytest.mark.django_db(transaction=True)
class Test01CoinsAPI:

    def test_01_coins_not_auth(self, client):
        response = client.get('/api/v1/coins/')
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            'Эндпоинт `/api/v1/coins/` не найден. Проверьте настройки в '
            '*urls.py*.'
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            '`/api/v1/coins/` возвращает ответ со статусом 200.'
        )

    def test_02_coins_with_user(self, user_client):
        coins_count = 0

        url = '/api/v1/coins/'
        data = {}
        response = user_client.post(url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f'Если POST-запрос, отправленный к `{url}`, '
            'содержит некорректные данные - должен вернуться ответ со '
            'статусом 400.'
        )

        data = {
            'code': 'BTC_1',
            'name': 'bitcoin',
            'price': '27',
            'total_supply': '121321',
            'percent_change': '11'
        }
        response = user_client.post(url, data=data)
        assert response.status_code == HTTPStatus.CREATED, (
            f'Если POST-запрос, отправленный к `{url}`, '
            'содержит корректные данные - должен вернуться ответ со статусом '
            '201.'
        )
        coins_count += 1

        post_data = {
            'code': 'BTC_1',
            'name': 'bitcoin',
            'price': '27',
            'total_supply': '121321',
            'percent_change': '11'
        }
        response = user_client.post(url, data=post_data)
        assert response.status_code == HTTPStatus.CREATED, (
            f'Если POST-запрос к `{url}` '
            'содержит корректные данные - должен вернуться ответ со статусом '
            '201.'
        )
        coins_count += 1

        response = user_client.get(url)
        assert response.status_code == HTTPStatus.OK, (
            f'Проверьте, что при GET-запросе к `{url}` возвращается статус '
            '200.'
        )

    def test_04_coins_check_permission_user(self,
                                            client,
                                            user_client):
        coins = create_coins(user_client)
        data = {
            'code': 'BTC_1',
            'name': 'bitcoin',
            'price': '27',
            'total_supply': '121321',
            'percent_change': '11'
        }
        url = '/api/v1/coins/'
        check_permissions(client, url, data, 'неавторизованного пользователя',
                          coins, HTTPStatus.UNAUTHORIZED)
        check_permissions(user_client, url, data,
                          'пользователя с ролью `user`', coins,
                          HTTPStatus.CREATED)
