from http import HTTPStatus

import pytest

from tests.utils import check_permissions, create_news


@pytest.mark.django_db(transaction=True)
class Test02NewsAPI:

    def test_01_news_not_auth(self, client):
        response = client.get('/api/v1/news/')
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            'Эндпоинт `/api/v1/news/` не найден. Проверьте настройки в '
            '*urls.py*.'
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к  '
            '`/api/v1/news/` возвращает ответ со статусом 200.'
        )

    def test_02_news(self, user_client, client):
        news_count = 0
        url = '/api/v1/news/'

        data = {}
        response = user_client.post(url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            f'Если POST-запрос к `{url}` '
            'содержит некорректные данные - должен вернуться ответ со '
            'статусом 400.'
        )

        data = {
            'author': 'Name',
            'description': 'Some Text',
            'title': 'Some title',
            'published': '2023-05-02'
        }
        response = user_client.post(url, data=data)
        assert response.status_code == HTTPStatus.CREATED, (
            f'Если POST-запрос к `{url}` содержит корректные '
            'данные - должен вернуться ответ со статусом 201.'
        )
        news_count += 1

        post_data = {
            'author': 'Name',
            'description': 'Some Text',
            'title': 'Some title',
            'published': '2023-05-02'
        }
        response = user_client.post(url, data=post_data)
        assert response.status_code == HTTPStatus.CREATED, (
            f'Если POST-запрос, отправленный к `{url}`, '
            'содержит корректные данные - должен вернуться ответ со статусом '
            '201.'
        )
        news_count += 1

        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{url}` возвращает ответ со статусом 200.'
        )
        data = response.json()

    def test_03_news_check_permission(self,
                                      client,
                                      user_client):
        news = create_news(user_client)
        data = {
            'author': 'Name',
            'description': 'Some Text',
            'title': 'Some title',
            'published': '2023-05-02'
        }
        url = '/api/v1/news/'
        check_permissions(client, url, data, 'неавторизованного пользователя',
                          news, HTTPStatus.UNAUTHORIZED)
        check_permissions(user_client, url, data,
                          'пользователя с ролью `user`', news,
                          HTTPStatus.CREATED)
