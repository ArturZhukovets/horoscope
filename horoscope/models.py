from django.db import models
from horoscope.description_request import open_file
# Create your models here.

content = open_file()


class Horoscope(models.Model):
    zodiac_name = models.CharField(max_length=30)
    horoscope_description = models.TextField()

    def __str__(self):
        return f'{self.zodiac_name}'

