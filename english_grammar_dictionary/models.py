from django.db import models
import json


class Dictionary(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50, null=True, default='')
    transcription = models.CharField(max_length=50, null=True, default='')
    context = models.TextField(default='')

    def __str__(self):
        return f'{self.word}'

#
# def open_json():
#     with open('C:\py\WEB-SCRAPING\englex_1000_words\eng_words.json', 'r', encoding='utf-8') as file:
#         content = json.load(file)
#     return content


