from http import HTTPStatus


def check_permissions(client, url, data, user_role, objects,
                      expected_status):

    response = client.post(url, data=data)
    assert response.status_code == expected_status, (
        f'Проверьте, что POST-запрос {user_role} к `{url}` возвращает ответ '
        f'со статусом {expected_status}.'
    )


def create_coins(user_client):
    data1 = {
        'code': 'BTC_1',
        'name': 'bitcoin',
        'price': '27',
        'total_supply': '121321',
        'percent_change': '11'
    }
    response = user_client.post('/api/v1/coins/', data=data1)
    assert response.status_code == HTTPStatus.CREATED, (
        'Если POST-запрос к `/api/v1/coins/` '
        'содержит корректные данные - должен вернуться ответ со статусом 201.'
    )
    data2 = {
        'code': 'BTC_2',
        'name': 'bitcoin',
        'price': '27',
        'total_supply': '121321',
        'percent_change': '11'
    }
    user_client.post('/api/v1/coins/', data=data2)
    return [data1, data2]


def create_news(user_client):
    result = []
    data = {
        'author': 'Name',
        'description': 'Some Text',
        'title': 'Some title',
        'published': '2023-05-02'
    }
    result.append(data)
    response = user_client.post('/api/v1/news/', data=data)
    assert response.status_code == HTTPStatus.CREATED, (
        'Если POST-запрос к `/api/v1/news/` содержит '
        'корректные данные - должен вернуться ответ со статусом 201.'
    )
    data = {
        'author': 'Name_1',
        'description': 'Some Text',
        'title': 'Some title',
        'published': '2023-05-02'
    }
    result.append(data)
    user_client.post('/api/v1/news/', data=data)
    data = {
        'author': 'Name_2',
        'description': 'Some Text',
        'title': 'Some title',
        'published': '2023-05-02'
    }
    result.append(data)
    user_client.post('/api/v1/news/', data=data)
    return result
