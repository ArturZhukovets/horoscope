import requests
import json


CITY_ID= 625144
API_WEATHER_KEY = '88a7a45d8205dfe8f6e0155c023d195d'
def request_how_to_know_city_id():
    s_city = "Minsk"
    city_id = 0
    appid = API_WEATHER_KEY
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass

def request_get_weather():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': API_WEATHER_KEY})
        data = res.json()
        print("Состояние:", data['weather'][0]['description'])
        print("Актуальная температура:", data['main']['temp'])
        print("Минимальная температура:", data['main']['temp_min'])
        print("Максимальная температура:", data['main']['temp_max'])
        print(data)
        # return(f"{data['weather'][0]['description']}"
        #        f"{data['main']['temp']}"
        #        f"{data['main']['temp_min']}"
        #        f"{data['main']['temp_max']}")
        return [data['weather'][0]['description'], data['main']['temp'], data['main']['temp_min'], data['main']['temp_max']]
    except Exception as e:
        print("Exception (weather):", e)
        pass


