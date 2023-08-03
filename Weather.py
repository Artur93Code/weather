import requests #jeśli wystąpi błąd braku modułu to należy zainstalować: (Windows) pip install requests


def checkWeather(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?units=metric&appid='
    with open('Api_key.txt') as f:
     api_key = f.readline()
     f.close()
	
    #city = input("Pogoda w (miasto): ")

    url = api_address + api_key + "&q=" + city

    json_data = requests.get(url).json() #konwersja pobranych danych do formatu json

    global temp

    lon = json_data['coord']['lon']
    lat = json_data['coord']['lat']
    temp = json_data['main']['temp']
    country_id = json_data['sys']['country']

    return [lon,lat,country_id,temp]

    #print(json_data)
    #print(temp)
    #print(country_id)

    #input("Koniec programus. Wciśnij dowolny przycisk")
