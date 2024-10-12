import requests
# імпортуємо модуль requests
from .read_json import read_json
# З файлу read_json імпортуємо функцію read_json
import json
# імпорткуємо модуль json
data_api = read_json(name_file= 'config_api.json')
#змінна з значеннням, яке знаходиться у функції read_json, в ній мається змінна яка має в собі дані файлу config_api.json
API_KEY = data_api['api_key']
# створена змінна з айпі, значення якої є айпі ключем введеним у файлі config_api.json
CITY_NAME = data_api['city_name']
# змінна з назвою міста 
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# посилання URL на сайт з погодою з виктористанням словників CITY_NAME та API_KEY
response = requests.get(URL)
# отримує дані за адресою URL
if response.status_code == 200:
    # Показує та перевіряє чи були отримані дані
    data_dict = json.loads(response.content)
    # перетворює отриманий байт у str
    print(json.dumps(data_dict, indent= 4))