"""ДАТА"""


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token
token = "7349600380:AAEogCt9ZMJ2_CTBIn7bNtf6Jgro7L2L4hs"

# Неиспользуемые номера кнопок - 8
# Buttons
# Нумерация кнопок происходит по тому когда я их создал
btn_choose_1 = [InlineKeyboardButton(text='Я хочу отдохнуть😎', callback_data='button1')]   # Choose the activity 1
btn_choose_2 = [InlineKeyboardButton(text='Я хочу изчучить что-то новое🤓', callback_data='button4')]   # Choose the activity 2
btn_choose_3 = [InlineKeyboardButton(text='Другое', callback_data='button3')]   # Choose the activity 3

btn_activity_1_1 = [InlineKeyboardButton(text='Выбрать случайный фильм🎥', callback_data='button2')]   # Act
btn_activity_1_2 = [InlineKeyboardButton(text='Выбрать случайную книгу📚', callback_data="button7")]   # Act

btn_activity_2_1 = [InlineKeyboardButton(text='Выбрать случайную тему для изучения🎓', callback_data='button5')]
btn_activity_2_2 = [InlineKeyboardButton(text='Выбрать случайную цитату🤫🧏‍♂️', callback_data='button6')]

buttons_kb1 = [btn_choose_1, btn_choose_2, btn_choose_3]   # List of variants Choose the activity
buttons_kb2 = [btn_activity_1_1, btn_activity_1_2]   # List of act I want to relax
buttons_kb3 = [btn_activity_2_1, btn_activity_2_2]   # I want to learn something new

button_replay_1_1 = [btn_activity_1_1]
button_replay_1_2 = [btn_activity_1_2]

button_replay_2_1 = [btn_activity_2_1]
button_replay_2_2 = [btn_activity_2_2]

button_replay_3 = [btn_choose_3]

# Keyboards
kb1 = InlineKeyboardMarkup(inline_keyboard=buttons_kb1)   # Choose the activity
kb2 = InlineKeyboardMarkup(inline_keyboard=buttons_kb2)   # List of act I want to relax
kb3 = InlineKeyboardMarkup(inline_keyboard=buttons_kb3)   # List of act I want to learn something new

kb_replay1_1 = InlineKeyboardMarkup(inline_keyboard=button_replay_1_1)
kb_replay1_2 = InlineKeyboardMarkup(inline_keyboard=button_replay_1_2)
kb_replay2_1 = InlineKeyboardMarkup(inline_keyboard=button_replay_2_1)
kb_replay2_2 = InlineKeyboardMarkup(inline_keyboard=button_replay_2_2)
kb_replay_3 = InlineKeyboardMarkup(inline_keyboard=button_replay_3)


algorithms = [["алгоритмы сортировок", "https://proglib.io/p/sort-gif"],
              ["метод двух указателей: ", "https://wcademy.ru/two-pointers-method/"],
              ["динамическое программирование: ", "https://habr.com/ru/articles/777618/"],
              ["графы: ", "https://habr.com/ru/companies/otus/articles/568026/"],
              ["present simple(Простое настоящее время)", "https://skysmart.ru/articles/english/present-simple-tense?ysclid=m63t5x1hci943239249"],
              ["future simple(Простое будующее время)", "https://skysmart.ru/articles/english/future-simple-tense?ysclid=m63t6qrs7b586027303"],
              ["present continuous(Настоящее продолжительное время)", "https://skysmart.ru/articles/english/present-continuous-tense?ysclid=m63tk0iuyb41518824"],
              ["past simple(Простое прошедшее время)", "https://skysmart.ru/articles/english/past-simple-tense?ysclid=m63ts5fupz160283138"]]


actions = ["сделать зарядку🏋️‍♂️",
           "прогуляться на улице🚶‍♂️",
           "пройти 3 задачи с информатикса(https://informatics.msk.ru/?redirect=0)💻",
           "сыграть в баскетбол🏀",
           "сыграть в футбол⚽️",
           "попробовать сделать музыку🎼",
           "сыграть в шахматы(https://www.c4355.com/ru/play/computer)♟️",
           "решить пару головоломок (пример сайт головоломками wordly: https://wordleplay.com/ru/)🧩",
           "убраться в доме🧹"]

# Список максимум
# Сделать красивое оформление вывода данных(предложение фильма) добавить смайлов и т.п.


"""
                Список литературы
https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html 25.12.2024
https://habr.com/ru/articles/820877/ 25.12.2024
https://www.youtube.com/watch?v=o06cdLnyc3I 26.12.2024
https://www.youtube.com/watch?v=cNb6WYNvxok&list=PLNi5HdK6QEmWLtb8gh8pwcFUJCAabqZh_ 23.12.2024
"""
