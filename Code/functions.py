from aiogram import types

types_rate = [
        [types.KeyboardButton(text="USD")],
        [types.KeyboardButton(text="EUR")],
        [types.KeyboardButton(text="Назад")]
    ]

matrix = [
    {'name': 'Сбер', 'usd': 0, 'eur': 1},
    {'name': 'Альфа', 'usd': 0, 'eur': 1},
    {'name': 'Тинькофф', 'usd': 0, 'eur': 1}
]

def get_time_function(message):
    date = message.date.strftime("%d.%m %H:%M")
    day, time = date.split()  # Разбиваем строку на составляющие
    hours, minutes = time.split(":")  # еще раз
    hours = (int(hours) + 5)
    return f"{day} {hours}:{minutes}"

def get_value_matrix(sber, alfa_tink):
    matrix[0]['usd'] = sber[0]
    matrix[0]['eur'] = sber[1]
    matrix[1]['usd'] = alfa_tink[0][1]
    matrix[1]['eur'] = alfa_tink[0][2]
    matrix[2]['usd'] = alfa_tink[1][1]
    matrix[2]['eur'] = alfa_tink[1][2]
