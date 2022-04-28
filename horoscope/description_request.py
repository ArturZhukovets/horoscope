import json


def open_file():
    with open(r'data/horoscope.json', 'r', encoding='utf-8') as file:
        kek = json.load(file)
    return kek


def open_horoscope_for_30_days():
    with open(r'C:\py\first\blog\data\horoscope_for_30_days.json', 'r') as file:
        horoscope_for_30_days = json.load(file)
    return horoscope_for_30_days

# for i in content:
#     for key, value in i.items():
#         Horoscope.objects.get(zodiac_name=key).update(horoscope_description=value)
