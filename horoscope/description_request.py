import json


def open_file():
    with open(r'data/horoscope.json', 'r', encoding='utf-8') as file:
        kek = json.load(file)
    return kek
