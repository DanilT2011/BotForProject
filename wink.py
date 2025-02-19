"""СБОРКА ФИЛЬМОВ ВИНК"""


import requests
from bs4 import BeautifulSoup as b


def giwink():
    """ФИЛЬМЫ С WINK"""
    films = soup.find_all('a', 'r17nqod8')
    return films


URL = "https://wink.ru/collections/besplatno"

r = requests.get(URL)
soup = b(r.text, 'html.parser')
