import json


def open_file():
    with open(r'C:\py\WEB-SCRAPING\parsZodiac\horoscope.json', 'r', encoding='utf-8') as file:
        kek = json.load(file)
    return kek
