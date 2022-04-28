from django.contrib import admin
from .models import Horoscope
# Register your models here.


class HoroscopeAdmin(admin.ModelAdmin):

    list_display = ['zodiac_name', 'horoscope_description', 'horoscope_on_30_days']
    list_editable = ['horoscope_description', 'horoscope_on_30_days']

admin.site.register(Horoscope, HoroscopeAdmin)  # Регистрируем класс и модель




