"""СБОРКА ФИЛЬМОВ ИВИ"""


import requests
from bs4 import BeautifulSoup as b


def givi(URL, begin):
    """ФИЛЬМЫ С IVI"""
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    films = soup.find_all('li', 'gallery__item gallery__item_virtual')[begin::]
    res = []
    for el in films:
        da = el.find("div", "nbl-poster__propertiesInfo").find("div", "nbl-poster__propertiesRow").text.split(", ")
        res.append("Название: " + el.find("span", "nbl-slimPosterBlock__titleText").text + "\n" +
                   "Оценка: " + el.find("div", "nbl-poster__propertiesRow").text + "\n" +
                   "Год создания: " + da[0] + "\n" +
                   "Место создания: " + da[1] + "\n" +
                   "Жанр: " + da[2])
    return res


def give_film():
    res =  [givi("https://www.ivi.ru/collections/free-movies", 0) +
           givi("https://www.ivi.ru/collections/free-movies/page2", 30) +
           givi("https://www.ivi.ru/collections/free-movies/page3", 60)]
    return res[0]
