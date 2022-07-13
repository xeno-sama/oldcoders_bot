from aiogram import types, md
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config
from datetime import datetime


async def helpComand(message: types.Message):

    await message.answer(md.text(
        md.bold('Список команд Деда-бота:'),
        md.text('🔸', md.bold('/инфо')),
        md.text('🔸', md.bold('/инфа')),
        md.text('🔸', md.bold('привет, деды')),
        md.text('🔸', md.bold('алиса, который час')),
        sep='\n',
    ))


@dp.message_handler()
async def echo(message: types.Message):

    locale = message.from_user.locale
    loc2 = message.from_user.id

    match message.text.lower():
        case "/инфо" | "/info" | "/information":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "/номета" | "/nometa":
            await message.answer("\n[Пожалуйста, не задавайте мета-вопросов в чате!](https://nometa.xyz/)", parse_mode='markdown')
        case "/get_message_id":
            await message.answer(message.chat.id)
        case "/инфа":
            await message.answer("[\n* Клуб дедов-программистов FAQ *\n\nВ этом репозитории находится полезная информация, собранная участниками чата. Дорожные карты(roadmaps), шпаргалки, ссылки на курсы и самые полезные статьи.\n\nЭлементарный уровень\n - Начало работы с Вебом\n - Язык программирования Python\n - Введение в программирование. Подборка материалов по остальным языкам.\n\nПродвинутый уровень\n - Все для веб-разработчика\n - Все для Python-разработчика\n - Пет-проекты разной сложности: ресурсы, идеи\n - Задачи для прокачки + тестовые задания\n\nМатериалы и ресурсы других ИТ-сообществ:\n - Что учить веб-разработчику. Разные гайды 2021\n - Карты развития Python 2021\n\nПрофессии\n - В тестировщики хочу, пусть меня научат!\n - Кто такие бизнес-аналитики и как стать БА?\n\nПолезное:\n - Git и GitHub\n - Как мы учим английский язык](https://github.com/OldCodersClub/faq)", parse_mode='markdown', disable_web_page_preview=True)
        case "алиса сколько времени?":
            await message.answer(message.from_user.full_name+", [\n* Клуб дедов-программистов FAQ *\n\nВ этом репозитории находится полезная информация, собранная участниками чата. Дорожные карты(roadmaps), шпаргалки, ссылки на курсы и самые полезные статьи.\n\nЭлементарный уровень\n - Начало работы с Вебом\n - Язык программирования Python\n - Введение в программирование. Подборка материалов по остальным языкам.\n\nПродвинутый уровень\n - Все для веб-разработчика\n - Все для Python-разработчика\n - Пет-проекты разной сложности: ресурсы, идеи\n - Задачи для прокачки + тестовые задания\n\nМатериалы и ресурсы других ИТ-сообществ:\n - Что учить веб-разработчику. Разные гайды 2021\n - Карты развития Python 2021\n\nПрофессии\n - В тестировщики хочу, пусть меня научат!\n - Кто такие бизнес-аналитики и как стать БА?\n\nПолезное:\n - Git и GitHub\n - Как мы учим английский язык](https://github.com/OldCodersClub/faq)", parse_mode='markdown', disable_web_page_preview=True)
        case "алиса, сколько времени?":
            await message.answer("Дед "+message.from_user.full_name+", по гринвичу "+datetime.now().strftime("%H ч %M мин"))
        case "/username":
            # check_language () #message.answer(check_language ())
            await message.answer(message.from_user.full_name)
        case "/userid":
            await message.answer(message.from_user.id)
        case "алиса, сколько время?":
            await message.answer("Э, слушай, дед "++message.from_user.full_name+", так некультурно говорить")
        case "алиса, который час?":
            await message.answer("Дед "+message.from_user.full_name+", ты такой культурный. По гринвичу "+datetime.today().strftime("%H ч %M мин"))
        case "привет, деды":
            await message.answer("И тобе привет, Cтарина "+message.from_user.full_name)
        case "/help":
            await helpComand(message)
        case "душнила":
            await message.answer("Э, поридж  "+message.from_user.full_name+", тут тебе деды, фильтруй базар ")

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет, Cтарина "+message.from_user.full_name)
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать, "+message.from_user.full_name + ",\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")
