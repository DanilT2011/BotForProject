"""НУЖНЫЕ ФУНКЦИИ"""


def find_digit(begin, l):
    """НАЙТИ ЧИСЛО"""
    for i in range(begin, len(l)):
        if l[i].isdigit():
            return i


def cln_mask_wink(l):
    try:
        name = "Название фильма: " + l[3:l.rfind(",") - 4] + "\n"
        score = "Оценка: " + l[0] + "." + l[2] + "\n"
        time = "Длительность: " + l[find_digit(l.rfind(","), l):l.rfind("мин") + 3]

        return "Взято с сайта wink\n" + name + score + time
    except:
        print("err")


def cln_mask_ivi(l):
    txt = l.text
    l = str(l)
    try:
        name = "Название фильма: " + l[l.rfind('Text"')+6:l.rfind("</span"):] + "\n"
        score = "Оценка: " + txt[0] + "." + txt[2] + "\n"
        da = l.rfind('esRow">')+7
        time = "Длительность: " + l[da:l.find("</div>", da)]
        return "Взято с сайта ivi\n" + name + score + time
    except:
        print("err")
