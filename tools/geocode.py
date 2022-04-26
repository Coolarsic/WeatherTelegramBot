import requests
from config import MAP_API
#  Далее код нагло стыренный с одного из уроков


def geocode(address):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": MAP_API,
        "geocode": address,
        "format": "json"}
    response = requests.get(geocoder_request, params=geocoder_params)
    #  получаем объект
    if response:
        json_response = response.json()
        #  если всё ок то берём json
    else:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {geocoder_request}
            Http статус: {response.status_code} ({response.reason})""")
        #  иначе генерим исключение и выбрасываем его
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    #  получаем данные о топониме
    return features[0]["GeoObject"] if features else None
    #  возвращаем объект топонима, если его нет, то возвращается None


def get_coords(address):
    toponym = geocode(address)
    #  получаем топоним по адресу
    if not toponym:
        return None, None
        #  если None, то и возвращаем None
    toponym_coodrinates = toponym["Point"]["pos"]
    #  получаем координаты
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    #  разбиваем на список
    return float(toponym_longitude), float(toponym_lattitude)
    #  возвращаем список координат