import requests
from bs4 import BeautifulSoup as bs

def weather_report(new_date, url, city):

    r = requests.get(url, headers={"User-Agent": ""})

    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')

        temps = soup.find_all('span', 'unit unit_temperature_c')
        temp = temps[6].text

        status = soup.find('div', 'now-desc')

        winds = soup.find('div','unit unit_wind_m_s')
        for i in winds:
            wind = i.text
            break

        press = soup.find('div', 'unit unit_pressure_mm_hg')
        for i in press:
            pres = i.text
            break

        humidity = soup.find('div','now-info-item humidity')

        report = (f'Прогноз погоды в городе <i>{city}</i> на {new_date}\n'
                  f'{status.text}\n'
                  f'<b>Температура:</b> {temp}\n'
                  f'<b>Ветер:</b> {wind} м/с\n'
                  f'<b>Давление:</b> {pres} мм\n'
                  f'<b>Влажность:</b> {humidity.text[6:]}\n')
        return (report)

    else:
        print('Error')

