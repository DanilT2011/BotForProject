"""РАНДОМНЫЙ ФАКТ"""


import requests
from bs4 import BeautifulSoup as b


def get_fact():
    """СЛУЧАЙНЫЙ ФАКТ"""
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    fact = soup.find('td').text
    autor = fact[fact.rfind("—")::]
    fact = fact[:fact.rfind("—"):]
    return [fact, autor]


URL = "https://randstuff.ru/saying/"
