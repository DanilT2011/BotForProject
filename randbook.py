"""РАНДОМНАЯ КНИГА"""


import requests
from bs4 import BeautifulSoup as b


def get_book():
    """СЛУЧАЙНАЯ КНИГА"""
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    book = soup.find_all('h3', 'blvi__title')
    info_book = soup.find_all('div', 'blvi__book_info')
    return book + info_book


URL = "https://readly.ru/books/i_am_lucky/?show=1"
