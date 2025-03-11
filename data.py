"""ДАТА"""


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token
token = "Это информация тут не нужна"

# Неиспользуемые номера кнопок - 14
# Buttons
# Нумерация кнопок происходит по тому когда я их создал
btn_choose_1 = [InlineKeyboardButton(text='Я хочу отдохнуть😎', callback_data='button1')]   # Choose the activity 1
btn_choose_2 = [InlineKeyboardButton(text='Я хочу изчучить что-то новое🤓', callback_data='button4')]   # Choose the activity 2
btn_choose_3 = [InlineKeyboardButton(text='Другое', callback_data='button3')]   # Choose the activity 3

btn_activity_1_1 = [InlineKeyboardButton(text='Выбрать случайный фильм🎥', callback_data='button2')]   # Act
btn_activity_1_2 = [InlineKeyboardButton(text='Выбрать случайную книгу📚', callback_data="button7")]   # Act
btn_activity_1_3 = [InlineKeyboardButton(text='Выбрать случайную мультфильм🎥', callback_data="button8")]

btn_activity_2_1 = [InlineKeyboardButton(text='Выбрать случайную тему для изучения🎓', callback_data='button5')]
btn_activity_2_2 = [InlineKeyboardButton(text='Выбрать случайную цитату🤫🧏‍♂️', callback_data='button6')]

btn_choose_18_1 = [InlineKeyboardButton(text='Я хочу отдохнуть😎', callback_data='button11')]   # Choose the activity 1
btn_choose_18_2 = [InlineKeyboardButton(text='Я хочу изчучить что-то новое🤓', callback_data='button12')]   # Choose the activity 2
btn_choose_18_3 = [InlineKeyboardButton(text='Другое', callback_data='button13')]      # Choose the activity 3

btn_choose_50_1 = [InlineKeyboardButton(text='Я хочу отдохнуть😎', callback_data='button14')]   # Choose the activity 1
btn_choose_50_2 = [InlineKeyboardButton(text='Я хочу изчучить что-то новое🤓', callback_data='button15')]   # Choose the activity 2
btn_choose_50_3 = [InlineKeyboardButton(text='Другое', callback_data='button16')]   # Choose the activity 3

age_btn18 = [InlineKeyboardButton(text='5-18 лет', callback_data='button9')]
age_btn50 = [InlineKeyboardButton(text='18-50 лет', callback_data='button10')]

buttons_kb1 = [btn_choose_1, btn_choose_2, btn_choose_3]   # List of variants Choose the activity
buttons_kb2 = [btn_activity_1_1, btn_activity_1_2, btn_activity_1_3]   # List of act I want to relax
buttons_kb3 = [btn_activity_2_1, btn_activity_2_2]   # I want to learn something new
buttons_kb4 = [age_btn18, age_btn50]   # Choose age

button_replay_1_1 = [btn_activity_1_1]
button_replay_1_2 = [btn_activity_1_2]
button_replay_1_3 = [btn_activity_1_3]

button_replay_2_1 = [btn_activity_2_1]
button_replay_2_2 = [btn_activity_2_2]

button_kb1_18 = [btn_choose_18_1, btn_choose_18_2, btn_choose_18_3]   # KB of recommend actions
button_kb2_18 = [btn_activity_1_2, btn_activity_1_3]   # 18 I want relax
button_kb3_18 = [btn_activity_2_1, btn_activity_2_2]   # 18 I want to learn something new

button_kb1_50 = [btn_choose_50_1, btn_choose_50_2, btn_choose_50_3]   # KB of recommend actions
button_kb2_50 = [btn_activity_1_2, btn_activity_1_1]   # 50 I want relax
button_kb3_50 = [btn_activity_2_2]   # 50 I want to learn something new

button_replay_3 = [btn_choose_3]

# Keyboards
kb1_1 = InlineKeyboardMarkup(inline_keyboard=buttons_kb1)   # Choose the activity
kb1_2 = InlineKeyboardMarkup(inline_keyboard=buttons_kb2)   # List of act I want to relax
kb1_3 = InlineKeyboardMarkup(inline_keyboard=buttons_kb3)   # List of act I want to learn something new
kb_age = InlineKeyboardMarkup(inline_keyboard=buttons_kb4)   # Choose age
kb1_18 = InlineKeyboardMarkup(inline_keyboard=button_kb1_18)   # 18 Age recommend
kb2_18 = InlineKeyboardMarkup(inline_keyboard=button_kb2_18)   # 18 Age recommend
kb3_18 = InlineKeyboardMarkup(inline_keyboard=button_kb3_18)   # 18 Age recommend
kb1_50 = InlineKeyboardMarkup(inline_keyboard=button_kb1_50)   # 18 Age recommend
kb2_50 = InlineKeyboardMarkup(inline_keyboard=button_kb2_50)   # 18 Age recommend
kb3_50 = InlineKeyboardMarkup(inline_keyboard=button_kb3_50)   # 18 Age recommend

kb_replay1_1 = InlineKeyboardMarkup(inline_keyboard=button_replay_1_1)   # Re-choose film
kb_replay1_2 = InlineKeyboardMarkup(inline_keyboard=button_replay_1_2)   # Re-choose book
kb_replay1_3 = InlineKeyboardMarkup(inline_keyboard=button_replay_1_3)   # Re-choose animated film (cartoon)
kb_replay2_1 = InlineKeyboardMarkup(inline_keyboard=button_replay_2_1)   # Re-choose тему для изучения
kb_replay2_2 = InlineKeyboardMarkup(inline_keyboard=button_replay_2_2)   # Re-choose random sentence
kb_replay2_3 = InlineKeyboardMarkup(inline_keyboard=button_replay_3)   # Re-choose Ofter


algorithms = [["алгоритмы сортировок", "https://proglib.io/p/sort-gif"],
              ["метод двух указателей: ", "https://wcademy.ru/two-pointers-method/"],
              ["динамическое программирование: ", "https://habr.com/ru/articles/777618/"],
              ["графы: ", "https://habr.com/ru/companies/otus/articles/568026/"],
              ["present simple(Простое настоящее время)", "https://skysmart.ru/articles/english/present-simple-tense?ysclid=m63t5x1hci943239249"],
              ["future simple(Простое будующее время)", "https://skysmart.ru/articles/english/future-simple-tense?ysclid=m63t6qrs7b586027303"],
              ["present continuous(Настоящее продолжительное время)", "https://skysmart.ru/articles/english/present-continuous-tense?ysclid=m63tk0iuyb41518824"],
              ["past simple(Простое прошедшее время)", "https://skysmart.ru/articles/english/past-simple-tense?ysclid=m63ts5fupz160283138"]]


actions_18 = ["сделать зарядку🏋️‍♂️",
             "прогуляться на улице🚶‍♂️",
             "пройти 3 задачи с информатикса(https://informatics.msk.ru/?redirect=0)💻",
             "сыграть в баскетбол🏀",
             "сыграть в футбол⚽️",
             "попробовать сделать музыку🎼",
             "убраться в доме🧹",
             "попробовать сделать монтаж для видео(https://hi-tech.mail.ru/review/59725-programmy-dlya-montazha/?ysclid=m7hcwk1ru1731991103#anchor172301922090088196)🎬"]


actions_50 = ["поспать 1-2 часа💤",
              "прогуляться на улице🚶‍♂️",
              "сыграть в шахматы(https://www.c4355.com/ru/play/computer)♟️",
              "решить пару головоломок (пример сайт головоломками wordly: https://wordleplay.com/ru/)🧩",
              "прочитать пару анекдотов(https://www.litres.ru/book/raznoe-47672/samye-smeshnye-anekdoty-23556560/chitat-onlayn/)",
              "приготовить что-то новое👨‍🍳",
              "убраться в доме🧹"]
