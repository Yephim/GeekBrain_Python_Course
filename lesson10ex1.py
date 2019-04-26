# Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
import requests
import json

def get_IATA_code(city):
    link = f'http://autocomplete.travelpayouts.com/places2?term={city}&locale=ru&types[]=city'
    res = requests.get(link)
    data=json.loads(res.text)
    if len(data) == 1:
        return data[0]["code"]
    elif len(data) == 0:
         return None
    elif len(data) > 0:
         d = {jcity['code']:jcity['name'].capitalize() for jcity in data if jcity['name'].capitalize() == city.capitalize()}
         if len(d)==1:
             for code, name in d.items():
                return code
         elif len(d) == 0:
             return None
         elif len(d) > 0:
             return list(d.keys())

print(get_IATA_code(input('Введите по-русски название города:')))