import requests
from bs4 import BeautifulSoup as BS

#id app > class global-wrapper > class app-content > class columns-wrapper > class inner-columns-wrapper > class central-right-wrapper > class central-column-container > class JTS1e > class _21ODi
url = "https://74.ru/horoscope/daily/"
r = requests.get(url)  #request a connection
html = BS(r.content, 'html.parser')  #say that we want to use html-parser

#selecting a text for today
a = html.select("#app > .global-wrapper > .app-content > .columns-wrapper > .inner-columns-wrapper > .central-right-wrapper > .central-column-container > .JTS1e > ._21ODi > ._2j-zP")

#input
zodiac = str(input("Введите ваш знак зодиака: "))

#dictionary of signs
dict = {"овен" : 0,
        "телец":1,
        "близнецы":2,
        "рак":3,
        "лев":4,
        "дева":5,
        "весы":6,
        "скорпион":7,
        "стрелец":8,
        "козерог":9,
        "водолей":10,
        "рыбы":11
        }

numb = dict[zodiac.lower()]  #id of goroskop
print("Ваш гороскоп на сегодня: " + a[numb].text)