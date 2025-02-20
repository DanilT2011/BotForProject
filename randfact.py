"""РАНДОМНАЯ ЦИТАТА"""


import requests
from bs4 import BeautifulSoup as b


def get_fact():
    """СЛУЧАЙНАЯ ЦИТАТА"""
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    fact = soup.find('td').text
    autor = fact[fact.rfind("—")::]
    fact = fact[:fact.rfind("—"):]
    return [fact, autor]


URL = "https://randstuff.ru/saying/"
