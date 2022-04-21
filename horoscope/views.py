from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Horoscope
from .models import update_horoscope_script
from horoscope.description_request import open_file


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}
types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):
    """Здесь создаю отображение главной страницы по url horoscope подробности реализации УРОК №17
    В качестве аргументов функции render выступает: request, html файл, context - словарь с контентом"""
    zodiacs = list(zodiac_dict)  # создаём список знаков зодиака
    # f"<li><a href='{redirect_path}'>{sign.title()} </a></li>"
    # li_elements = ''  # создаём результирующую строку
    # for sign in zodiacs:
    #     redirect_path = reverse('horoscope-name',args=(sign,))  # в каждой итерации создаём путь url на каждый знак зодиака
    #     li_elements += f"<li><a href='{redirect_path}'>{sign.title()} </a></li>"  # подставляем в результирующую строку знак зодиака в теге <list> и добавляем ссылку с юрлом {redirect_pass}
    # response = f'''
    # <ol>
    #     {li_elements}
    # </ol>
    # '''
    # return HttpResponse(response)
    context = {
        "zodiacs": zodiacs,  # В ключе zodiacs лежит список из ключей словаря со знаками зодиака
        "zodiac_dict": zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)  # аргумент context является словарём context


def info_about_type_of_sign_of_zodiac(request):
    """Здесь создаем НЕ динамическую вьюху, в которой будут храниться существующие типы знаков"""
    # types_of_zodiac_list = ["fire", "earth", "air", "water"]
    li_types = ''

    for type in types_dict.keys():
        href_url = reverse('one-of-four', args=(type,))
        li_types += f"<li><a href='{href_url}'>{type.title()}</a></li>"
    response = f'''
        <ul>
        {li_types}
        </ul>
                '''
    return HttpResponse(response)


def one_of_type(request, type_zodiac: str):
    """Здесь будет отображатсья по три знака каждого типа: Огня, Воды, Земли, Воздуха. Создаём через ДИНАМИЧЕСКУЮ юрлу"""

    values = types_dict.get(type_zodiac)
    if values is not None:
        li_types = ''
        for type in values:
            type_href = reverse('horoscope-name', args=(type,))
            li_types += f'<li><a href="{type_href}">{type}</a></li>'
        response = f'''
        <ul>
            {li_types}
        </ul>
                    '''
        return HttpResponse(response)

    else:
        return HttpResponseNotFound(f'Введен неверный тип зодиака: <strong>{values}</strong>')


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    """Функция render_to_string читает html файл и преобразовывает его в строку (и отправляем его в видео HttpResponse)
    Но можно воспользоваться функцией render, которая заменяет собой всё вышенаписанное
    Очень важно понять, что render() использует 3ей переменной context, в которую я передаю данные в виде словаря
    И в словаре ключ - это переменная, которую мы передаем в шаблон! А значение этого ключа = это значение, которое будет отображаться"""
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)
    update_horoscope_script()
    horoscope_from_db = Horoscope.objects.get(zodiac_name=sign_zodiac)


    description = zodiac_dict.get(sign_zodiac)  # В переменной мы обращаемся к словарю и берем значение используя вместо ключа введённое пользователем значение.
    data = {
        'sign': sign_zodiac,
        'description_zodiac': description,  # Ключи в созданном словаре, будут являтся переменными в html шаблоне!
        'zodiacs': zodiac_dict,
        'horoscope': horoscope_from_db

    }
    return render(request, 'horoscope/info_zodiac.html',
                  context=data)  # Через аргумент context я передаю данные в виде словаря


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    """Здесь создаётся функция, которая редиректит запрос в строке юрла. Мы вводим номер знака зодиака и нас
    редиректит на значение этого номера по индексу"""
    zodiac_list = list(zodiac_dict)  # создаем список из ключей словаря
    if sign_zodiac > len(
            zodiac_list):  # если введенное пользователем число больше чем количество имеющихся ключей - ебашит ошибку
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака: {sign_zodiac}')
    name_zodiac = zodiac_list[
        sign_zodiac - 1]  # переменная, хранящая в себе исключительно ключ словаря (минусуем единицу, потому что индексы начинаются с нуля офк)
    redirect_url = reverse('horoscope-name', args=(
    name_zodiac,))  # Функция reverse воссоздаёт Весь url. Т.е результатом будет сконструированный url по которому надо перейти.
    return HttpResponseRedirect(redirect_url)  # перенаправляет на значение словаря по индексу
    # Можно обойтись и без редиректа, создав переменную в которой хранится значение словаря, а вместо ключа
    # выступает name_zodiac, полученная из индекса
    # description = zodiac_dict.get(name_zodiac)
    # return HttpResponse(description)  # перенаправляет на значение словаря по индексу фывофолывл


def get_info_by_date(request, mounth, day):
    return HttpResponse(f'<h2>Месяц - {mounth} День - {day}')


def get_horoscope_for_30_days(request, sign_zodiac: str, zodiac_slug: str):

    horoscope_for_30_days = Horoscope.objects.get(zodiac_name=sign_zodiac, slug=zodiac_slug)
    context = {
        'horoscope_for_30_days': horoscope_for_30_days

    }
    return render(request, 'horoscope/horoscope_for_30_days.html', context=context)

