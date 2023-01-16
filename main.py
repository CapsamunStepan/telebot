import logging
from aiogram import Bot, Dispatcher, executor, types
from BoyerMoore import boyer_moore, time_of_method1
from RabinCarp import rabin_carp, time_of_method2
from FiniteAutomata import finite_automata, time_of_method3, match
from KnuthMorrisPratta import knuth_morris_pratt, time_of_method4

API_TOKEN = '5780232055:AAHF5Va6B46QYaIegvy2XQ0ZGRu440rpZG0'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

list1 = []

button_new = "/new"
button1 = "1"
button2 = "2"
button3 = "3"
button4 = "4"
kb = [[types.KeyboardButton(text="/new"),
           types.KeyboardButton(text="1"),
           types.KeyboardButton(text="2"),
           types.KeyboardButton(text="3"),
           types.KeyboardButton(text="4")]]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

@dp.message_handler(commands=['start', 'new'])
async def send_welcome(message: types.Message):
    idi = message.from_user.id
    list1.clear()
    await message.answer("Привет!\nЯ бот поиска подстроки в строке.\nСделан на модуле aiogram.")
    await message.answer("Доступные методы: ")
    await message.answer("1. Алгоритм Бойера-Мура\n"
                         "2. Алгоритм Рабина-Карпа\n"
                         "3. Алгоритм конечных автоматов\n"
                         "4. Алгоритм Кнута-Морриса-Пратта")
    print(type(idi))
    await bot.send_message(idi, "Введите строку")


@dp.message_handler()
async def first(msg: types.Message):
    identificator = msg.from_user.id
    with open("input.txt", "a") as file:
        file.write(msg.from_user.full_name + " " + str(identificator) + "\n")
        file.write(msg.text + "\n")
    list1.append(msg.text)
    print(list1)
    if len(list1) < 2:
        await bot.send_message(msg.from_user.id, "Введите подстроку:")
    elif 1 < len(list1) < 3:
        await bot.send_message(msg.from_user.id, "Выберите метод.", reply_markup=keyboard)
    elif len(list1) > 2:
        if msg.text in ["1", "2", "3", "4"]:
            list1[2] = msg.text
        text = list1[0]
        pattern = list1[1]
        method = list1[2]
        i = 0
        if int(method) == 1:
            spisok = boyer_moore(pattern, text)
            for i in range(len(spisok)):
                await msg.answer(spisok[i])
            await msg.answer(str("%.10f" % time_of_method1()) + " сек")

        elif int(method) == 2:
            spisok = rabin_carp(pattern, text)
            for i in range(len(spisok)):
                await msg.answer(spisok[i])
            await msg.answer(str("%.10f" % time_of_method2()) + " сек")

        elif int(method) == 3:
            spisok = match(pattern, text)
            for i in range(len(spisok)):
                await msg.answer(spisok[i])
            await msg.answer(str("%.10f" % time_of_method3()) + " сек")

        elif int(method) == 4:
            spisok = knuth_morris_pratt(pattern, text)
            for i in range(len(spisok)):
                await msg.answer(spisok[i])
            await msg.answer(str("%.10f" % time_of_method4()) + " сек")

        else:
            await msg.answer("Метод выбран неправильно!!!")

        await bot.send_message(msg.from_user.id, "Выберите метод.", reply_markup=keyboard)
    await msg.answer(" ", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
