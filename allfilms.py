"""СБОРКА ФИЛЬМОВ"""


from IVI import givi
from wink import giwink
from function import cln_mask_ivi, cln_mask_wink


def build_list_films():
    clean_films = []   # Фильмы без ненужного

    for el in givi():
        clean_films.append(str(cln_mask_ivi(el)))
        print(clean_films[-1])

    for el in giwink():
        clean_films.append(str(cln_mask_wink(el.text)))
        print(clean_films[-1])

    return clean_films
