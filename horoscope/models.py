from django.db import models
from horoscope.description_request import open_file
from scriptparse import get_data
# Create your models here.


class Horoscope(models.Model):
    zodiac_name = models.CharField(max_length=30)
    horoscope_description = models.TextField()

    def __str__(self):
        return f'{self.zodiac_name}'


def update_horoscope_script(file=open_file()):
    """Наконец-то запилил функцию с обновлением БД. Не знаю правильно она реализована или нет, оно и не важно пока, главное, что работает.
    Когда будут знания как сделать правильно - сделаю правильно. Функция открывает json файл, который я запарсил с сайта и на основе данных обновляет БД"""

    for horoscope in file:
        for key, value in horoscope.items():
            new_horoscope = Horoscope.objects.get(zodiac_name=key)
            new_horoscope.horoscope_description = value
            new_horoscope.save()