from aiogram.filters.command import Command
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from parser_rate import *
from functions import *
from parser_weather import weather_report

TOKEN = ""
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
@dp.message(F.text.lower() == "назад")
async def cmd_start(message: types.Message):
    bt = [
    [types.KeyboardButton(text="Погода")],
    [types.KeyboardButton(text="Валюта")]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=bt, resize_keyboard=True, input_field_placeholder="Выбери действие",row_width=2)

    await message.answer("Начнём!", reply_markup=markup)

# Нажатие на кнопку валюта
@dp.message(F.text.lower() == "валюта")
async def cmd_rate(message: types.Message):
    global types_rate

    frst = asyncio.create_task(get_alfa_tink_rate())
    scnd = asyncio.create_task(get_sber_rate())

    await asyncio.gather(frst, scnd)

    alfa_tink = frst.result()
    sber =  scnd.result()

    get_value_matrix(sber, alfa_tink)

    markup = types.ReplyKeyboardMarkup(keyboard=types_rate, resize_keyboard=True, input_field_placeholder="Выбери валюту")
    await message.answer("Выбери валюту", reply_markup=markup)


# Выбор валюты
@dp.message((F.text.lower() == "usd") | (F.text.lower() == "eur"))
async def cmd_money(message: types.Message):
    global types_rate
    global matrix
    rate = [""]
    rate[0] = message.text.lower()

    new_date = get_time_function(message)

    answer = (f"Курс <i>{rate[0].upper()}</i> на {new_date} \n"
              f"<b>{matrix[0]['name']}</b>: {matrix[0][rate[0]]} рублей \n"
              f"<b>{matrix[1]['name']}</b>: {matrix[1][rate[0]]} рублей\n"
              f"<b>{matrix[2]['name']}</b>: {matrix[2][rate[0]]} рублей\n")

    markup = types.ReplyKeyboardMarkup(keyboard=types_rate, resize_keyboard=True, input_field_placeholder="Выбери валюту")
    await message.answer(answer, reply_markup=markup, parse_mode='html')


# Нажатие на кнопку погода
@dp.message(F.text.lower() == "погода")
async def cmd_rate(message: types.Message):
    url = ''
    url2 = ''
    new_date = get_time_function(message)
    city1 = weather_report(new_date, url, '')
    city2 = weather_report(new_date, url2, '')

    back = types.KeyboardButton(text='Назад')
    markup = types.ReplyKeyboardMarkup(keyboard=[[back]], resize_keyboard=True, input_field_placeholder="Назад")
    await message.answer(city1, reply_markup=markup, parse_mode='html')
    await message.answer(city2, reply_markup=markup, parse_mode='html')

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())