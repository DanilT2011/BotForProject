"""СБОРКА ВСЕГО, КОД БОТА"""

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
import data
from random import randint
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from allfilms import build_list_films
from randbook import get_book
from randfact import get_fact

TOKEN = data.token
bot = Bot(token=TOKEN)
films = build_list_films()  # Фильмы

dp = Dispatcher()


@dp.callback_query(lambda c: c.data == 'button1')   # Я хочу отдохнуть
async def process_callback_button1(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer("Вот, что я могу предложить вам:", reply_markup=data.kb2)


@dp.callback_query(lambda c: c.data == 'button2')   # Выбрать фильм
async def process_callback_button2(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer(films[randint(0, len(films))])
    await callback_query.message.answer("Перевыбрать фильм: ", reply_markup=data.kb_replay1_1)



@dp.callback_query(lambda c: c.data == 'button3')   # Другое
async def process_callback_button3(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer("Я могу предложить вам " + data.actions[randint(0, len(data.actions)-1)])
    await callback_query.message.answer("Перевыбрать занятие: ", reply_markup=data.kb_replay_3)


@dp.callback_query(lambda c: c.data == 'button5')   # Выбрать случайную тему для изучения
async def process_callback_button5(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    random_num = randint(0, len(data.algorithms) - 1)
    await callback_query.message.answer("Я могу предложить вам изучить " +
                                        data.algorithms[random_num][0] +
                                        "\nВот ссылка на материал: " + data.algorithms[random_num][1]
                                        )
    await callback_query.message.answer("Перевыбрать тему: ", reply_markup=data.kb_replay2_1)


@dp.callback_query(lambda c: c.data == 'button4')   # Я хочу узнать что-то новое
async def process_callback_button4(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await callback_query.message.answer("Вот, что я могу предложить вам:", reply_markup=data.kb3)


@dp.callback_query(lambda c: c.data == 'button6')   # Случайная цитата
async def process_callback_button6(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    res = get_fact()
    await callback_query.message.answer(res[0] + "\n" + res[1])
    await callback_query.message.answer("Перевыбрать цитату: ", reply_markup=data.kb_replay2_2)


@dp.callback_query(lambda c: c.data == 'button7')   # Книга
async def process_callback_button7(callback_query: CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    book = get_book()
    book1 = book[0].text
    book2 = book[1].text.split()
    await callback_query.message.answer("Вот, что я могу предложить вам: " + "\n" + "Название: " + book1 +
                                        "Автор: " + book2[0] + " " + book2[1] + "\n" +
                                        "Дата создания: " + book2[2] + book2[3] + "\n"
                                        "Жанр: " + book2[4] + "\n"
                                        "Взято с сайта readly")
    await callback_query.message.answer("Перевыбрать книгу: ", reply_markup=data.kb_replay1_2)



@dp.message(Command('freetime'))   # Начать генерацию занятия
async def choose_activity(message: Message):
    await message.reply("Что больше всего ты сейчас хочешь сделать?", reply_markup=data.kb1)


@dp.message(CommandStart())
async def command_start_handler(message: Message):   # Старт
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer("Чтобы узнать болше о боте напиши /info\n" +
                         "Чтобы начать генерацию занятия на свободное время напиши /freetime")


@dp.message(Command('info'))
async def say_informathion(message: Message):
    await message.answer("Данный бот создан учеником 7А класса Тян Данилом для проекта\n" +
                         "При написании команды /freetime бот генерирует занятие на свободное действие\n" +
                         "Бот парсит информацию с таких сайтов, как:\n" +
                         "https://www.ivi.ru/collections/free-movies\n" +
                         "https://wink.ru/collections/besplatno\n" +
                         "https://randstuff.ru/saying/\n" +
                         "https://readly.ru/books/i_am_lucky/?show=1")


@dp.message()
async def echo_handler(message: Message):
    await message.answer("Команды /freetime /info /start")


async def main():   # Запускается при запуске программы
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

