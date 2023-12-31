dic_que = {
    "Сколько зубов у взрослого человека": [["24", "29", "30", "31", "32"], "32"],
    "Сколько месяцев в году имеют 28 дней?": [["1", "2", "6", "0", "Все"], "Все"],
    "Сколько планет в Солнечной системе?": [["7", "8", "9", "10", "8"], "8"],
    "Сколько костей в человеческом теле?": [["100", "206", "300", "400", "206"], "206"],
    "Сколько цветов в радуге?": [["5", "6", "7", "8", "0"], "7"],

    "Сколько дней в неделе?": [["5", "6", "7", "8", "0"], "7"],

    "Сколько лет длилась Великая Отечественная война?": [["2", "4", "6", "8", "5"], "4"],

    "Сколько дней в феврале в високосный год?": [["27", "28", "29", "30", "29"], "29"],
    "Сколько клавиш на фортепиано?": [["64", "76", "88", "100", "88"], "88"],
    "Сколько букв в английском алфавите?": [["24", "26", "28", "30", "25"], "26"],
    "Сколько пальцев на руке у человека?": [["3", "4", "55", "6", "5"], "5"],
    "Выберите столицу Беларуси": [["Минск", "Полоцк", "Прага", "Вильнюс", "Витебск"], "Минск"],
    "Выберите столицу Украины": [["Киев", "Москва", "Львов", "Одесса", "Харьков"], "Киев"],
    "Выберите столицу России": [["Москва", "Санкт-Петербург", "Киев", "Минск", "Владивосток"], "Москва"],
    "Выберите столицу Франции": [["Париж", "Марсель", "Лион", "Тулуза", "Ницца"], "Париж"],
    "Выберите столицу Германии": [["Берлин", "Мюнхен", "Гамбург", "Франкфурт", "Кёльн"], "Берлин"],
    "Выберите столицу Италии": [["Рим", "Милан", "Неаполь", "Турин", "Флоренция"], "Рим"],
    "Выберите столицу Турции": [["Анкара", "Стамбул", "Анталья", "Измир", "Бурса"], "Анкара"],
    "Выберите столицу Китая": [["Пекин", "Шанхай", "Гуанчжоу", "Шэньчжэнь", "Тяньцзинь"], "Пекин"],


    "Выберите столицу Великобритании": [["Лондон", "Манчестер", "Бирмингем", "Ливерпуль", "Глазго"], "Лондон"],
    "Выберите столицу Канады": [["Оттава", "Торонто", "Монреаль", "Ванкувер", "Калгари"], "Оттава"],
    "Выберите столицу Бразилии": [["Бразилиа", "Сан-Паулу", "Рио-де-Жанейро", "Сальвадор", "Белу-Оризонти"],
                                  "Бразилиа"],
    "Какой метод используется для удаления элемента из списка в Python?": [
        ["remove()", "delete()", "discard()", "pop()", "remove()"], "remove()"],
    "Какой модуль используется для работы с датами и временем в Python?": [
        ["time", "datetime", "dateutil", "timedelta", "datatime"], "datetime"],
    "Что такое PIP в контексте Python?": [
        ["Интерпретатор", "Менеджер пакетов", "Рекомендации по стилю кода", "Библиотека", "Менеджер управления"],
        "Менеджер пакетов"],
    "Какой оператор используется для остатка от деления в Python?": [["/", "//", "%/", "*", "%"], "%"],
    "Как называется инструкция, которая позволяет прервать выполнение цикла в Python?": [
        ["break", "stop", "exit", "end", "brek"], "break"],
    "Как создать кортеж в Python?": [["(1, 2, 3,,)", "[1, 2, 3]", "{1, 2, 3}", "1, 2, 3", "(1, 2, 3)"], "(1, 2, 3)"],
    "Какая функция используется для получения длины списка в Python?": [
        ["size()", "length()", "len()", "count()", "len"], "len()"],
    "Что такое индексация в контексте Python?": [
        ["Процесс разделения строки на подстроки", "Процесс поиска подстроки в строке",
         "Процесс превращения строки в список", "Система нумерации элементов массива"], "Система нумерации элементов массива"],
    "Какой оператор используется для проверки вхождения элемента в список в Python?": [
        ["in", "not in", "contains", "has", "in()"], "in"],
    "Как создать словарь в Python?": [
        ["{} - пустой словарь", "[] - пустой словарь", "dict() - пустой словарь", "{key: value}",
         "{none} - пустой словарь"], "{} - пустой словарь"],
    "Какой синтаксис используется для создания функций в Python?": [["def", "fun", "function", "define", "def:"], "def"],
    "Какой символ используется для комментариев в Python?": [["//", "/*", "##", "--", "#"], "#"],
    "Какая версия Python является актуальной на данный момент?": [
        ["Python 2", "Python 3", "Python 3.5", "Python 3.8", "Python 3.9"], "Python 3.8"],
"Какая функция используется для вывода текста на экран в Python?": [
        ["print()", "echo()", "display()", "show()", "print"], "print()"],
    "Как создать пустой список в Python?": [["list[]", "list()", "list{}", "list<>", "list"], "list()"],
    "Какие типы данных поддерживает Python?": [
        ["int, float, str", "int, str, list", "int, float, str, list, dict", "int, float, str, list, dict, tuple",
         "int, float, str, list, dict, tuple,double"], "int, float, str, list, dict, tuple"],
    "Что такое PEP 8 в контексте Python?": [
        ["Рекомендации по стилю кода", "Интерпретатор", "Файл с расширением .py", "Стандартная библиотека"], "Рекомендации по стилю кода"],
    "Какой оператор используется для проверки равенства в Python?": [["==", "=", "===", "!=", "=()"], "=="],
    }



correct=["Ого, ну ты удивляешь!", "Умничка","Умняшка","Вы соверешенно правы,молодец","Ты абсолютно прав, в этом деле тебе нет равных!","Ничего себе!А ты ничего!!Хорошо справляешься"]
wrong=["Такие вопросы явно тебе не по зубам!","Ооооох, тяжело идешь...","Ну ты совсем не справляешься", "Сначала учебник  почитай!!","Не стыдно такое не знать?","Ты не прав."]

import telebot
import random
botQuizz = telebot.TeleBot("6883189131:AAEG5wYMXiBDQV08CAa8ZKTVfNnIj0m2ix0")
from telebot import types
import sqlite3
point=0



keys=list(dic_que.keys())
@botQuizz.message_handler(commands=['start'])
def start(start):
    global point
    point=0
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_go=types.KeyboardButton("/начать")
    markup.add(btn_go)
    botQuizz.send_message(start.chat.id, f"Ваш счет:{point}\nУспешной игры,будьте внимательны\n", parse_mode='html',reply_markup=markup)
@botQuizz.message_handler(commands=['начать','next'])
def start(function_call):
    key=random.choice(keys)
    question = f"\n{key}"
    markup = types.InlineKeyboardMarkup()
    for ans in dic_que[key][0]:
        btn = types.InlineKeyboardButton(text=ans, callback_data=ans)
        markup.add(btn)
    botQuizz.send_message(function_call.chat.id,question, parse_mode='html', reply_markup=markup)
    botQuizz.answer_callback_query(function_call.id)
@botQuizz.message_handler(commands=['end'])
def end(end):
    global point
    markup=types.replyKeyboardMarkup(resize_keyboard=True)
    btn_ = types.KeyboardButton("/начать")
    markup.add(btn_)
    botQuizz.send_message(end.chat.id,f"Решили сдаться? Ваш счет {point}, /начать - начать сначала" , parse_mode='html', reply_markup=markup)
    botQuizz.answer_callback_query(end.id)
@botQuizz.callback_query_handler(func=lambda call: True)
def call(mes):
    global point
    if mes.data==dic_que[ mes.message.text.strip('\n')][1]:
        point+=1
        botQuizz.send_message(mes.message.chat.id, f"{random.choice(correct)}\n\nВаш счет:{point}\n/начать - перейти к след вопросу\n\n/start-начать сначала ")
        botQuizz.answer_callback_query(mes.id)
    else:
        point-=1
        botQuizz.send_message(mes.message.chat.id,  f"{random.choice(wrong)}\n\nВаш счет:{point}\n/начать - перейти к след вопросу\n\n/start-начать сначала")
        botQuizz.answer_callback_query(mes.id)


botQuizz.infinity_polling()