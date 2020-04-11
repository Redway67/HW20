import requests
from bs4 import BeautifulSoup

url = f'https://pogoda.mail.ru/prognoz/anapa'


def get_weather(request):
    response = requests.get(url)
    answer = 'Всегда хорошая погода'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find_all('div', class_="information__content__temperature")
        today_temperature = temperature[0].text.split()[0]
        answer = f'В городе Анапа сейчас {today_temperature}.'
    return {'weather': f'{answer}'}
