"""РАНДОМНАЯ МУЛЬТФИЛЬМ"""


import requests
from bs4 import BeautifulSoup as b


def get_cartoons():
    """СЛУЧАЙНАЯ МУЛЬТФИЛЬМ"""
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    cartoon = soup.find_all("div", "p-itemevent-small js-event margin_bottom_30")
    res = []
    for el in cartoon:
        da = el.find("div", "margin_top_5").text.split(", ")
        res.append("Название: " + el.find("span", "link__text").text + "\n" +
                   "Место создания: " + da[0] + "\n" +
                   "Год создания: " + da[1] + "\n" +
                   "Жанры: " + ", ".join(da[2::]))
    return res


URL = "https://kino.mail.ru/cinema/all/multiplikacionnyj/"
