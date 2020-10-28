import requests


def get_html(url):
    """Функция возвращает HTML-страницу по URL-адресу

    Аргументы:
    :param: url -- URL-адрес страницы
    :return: HTML-страница
    """
    response = requests.get(url)
    return response.text
