"""СБОРКА ФИЛЬМОВ ИВИ"""


import requests
from bs4 import BeautifulSoup as b


def givi():
    """ФИЛЬМЫ С IVI"""
    films = soup.find_all('li', 'gallery__item gallery__item_virtual')
    return films


URL = "https://www.ivi.ru/collections/free-movies"

r = requests.get(URL)
soup = b(r.text, 'html.parser')
