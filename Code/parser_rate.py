import requests
from bs4 import BeautifulSoup as bs


async def get_alfa_tink_rate():
    url = ''
    r = requests.get(url)

    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')
        bank = soup.find_all('a', 'bank_link')
        usd_sell = soup.find_all('td', 'curr_hid USD')
        eur_sell = soup.find_all('td', 'curr_hid EUR')

        my_bank = []
        answer = []
        for i in range(0, len(bank)-1):
            if 'Альфа-Банк' == bank[i].text or 'Т-Банк' == bank[i].text:
                my_bank.append([bank[i].text, i])

        for i in range(len(my_bank)):
            answer.append((my_bank[i][0], usd_sell[my_bank[i][1]*2+1].text, eur_sell[my_bank[i][1]*2+1].text))
        return answer

    else: return 'Error'

async def get_sber_rate():
    url = ''
    r = requests.get(url)

    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')
        rates = soup.find_all('div', 't_cell')
        sber = []

        for i in range(len(rates)-1):
            if 'Доллар США' in rates[i].text or 'Евро' in rates[i].text:
                sber.append(rates[i+2].text)
        return sber

    else:
        return 'Error'
