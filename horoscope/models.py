from django.db import models
from horoscope.description_request import open_file, open_horoscope_for_30_days
from django.utils.text import slugify
from scriptparse import get_data
# Create your models here.


class Horoscope(models.Model):
    zodiac_name = models.CharField(max_length=30)
    horoscope_description = models.TextField(null=True)
    slug = models.SlugField(default='', max_length=20)
    horoscope_on_30_days = models.TextField(null=True)

    def save(self, *args, **kwargs):
        """Переопределил метод save для того, чтобы добавить всем полям slug новое значение. Обновленный метод save
        срабатывает в методе update_horoscope_script"""
        self.slug = slugify(self.zodiac_name)
        super(Horoscope, self).save(*args, **kwargs)  # Я хз что эта функция делает, надо будет разобраться

    def __str__(self):
        return f'{self.zodiac_name}'


    # def horoscope_description(self):
    #     return Horoscope.objects.get(zodiac_name=self)


def update_horoscope_script(file=open_file()):
    """Наконец-то запилил функцию с обновлением БД. Не знаю правильно она реализована или нет, оно и не важно пока, главное, что работает.
    Когда будут знания как сделать правильно - сделаю правильно. Функция открывает json файл, который я запарсил с сайта и на основе данных обновляет БД"""

    for horoscope in file:
        for key, value in horoscope.items():
            new_horoscope = Horoscope.objects.get(zodiac_name=key)
            new_horoscope.horoscope_description = value
            new_horoscope.save()

# for i in cont:
#     for key, value in i.items():
#         obnova = Horoscope.objects.get(zodiac_name=key)
#         obnova.horoscope_on_30_days = value
#         obnova.save()
