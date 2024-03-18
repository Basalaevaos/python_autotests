import requests

TOKEN = '5d11d92de68b0091ee5af0a2450ccc56'
URL = 'https://api.pokemonbattle.me/v2'
HEADER1 = {'trainer_token' : '5d11d92de68b0091ee5af0a2450ccc56'}
HEADER2 = {'Content-Type': 'application/json'}
HEADERS = {**HEADER1, **HEADER2}


#Создать покемона
BODY_CREATE = {
  "name": "Бульбазавр",
  "photo": "https://dolnikov.ru/pokemons/albums/001.png"
  }
respons = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json= BODY_CREATE)
print(respons.text)


#Изменить имя покемона
BODY_NAME = {
    "pokemon_id": "14272",
    "name": "Свин"
}
respons = requests.patch(url = f'{URL}/pokemons', headers = HEADERS, json= BODY_NAME)
print(respons.text)


#Поймать покемона в покебол
BODY_POKEBOL = {
    "pokemon_id": "14272"
}
respons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json= BODY_POKEBOL)
print(respons.text)








