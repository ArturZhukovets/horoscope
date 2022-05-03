from django.contrib import admin
from .models import Horoscope
from django.db.models import QuerySet
from .models import Horoscope, update_horoscope_script

# Register your models here.


@admin.register(Horoscope)
class HoroscopeAdmin(admin.ModelAdmin):

    list_display = ['zodiac_name', 'horoscope_description', 'horoscope_on_30_days']
    list_editable = ['horoscope_description', 'horoscope_on_30_days']
    actions = ['get_data']
# admin.site.register(Horoscope, HoroscopeAdmin)  # Регистрируем класс и модель

    @admin.action(description='Обновить гороскоп')  # Описание в админке
    def get_data(self, request, qs: QuerySet):
        """ Скрипт-пердун, но он работает. При активации в админке действия
         "обновить гороскоп" делается запрос на сайт
         с гариком, парсятся данные, а затем вызывается скрипт с обновой
          гарика и ву-аля гарики на сегодняшний день готовы """
        qs.update(horoscope_description=Horoscope.function_caller())
        update_horoscope_script()

        self.message_user(
            request,
            "Был обновлен горскоп на сегодня"
        )




