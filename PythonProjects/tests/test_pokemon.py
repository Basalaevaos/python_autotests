import requests
import pytest

TOKEN = '5d11d92de68b0091ee5af0a2450ccc56'
URL = 'https://api.pokemonbattle.me/v2'
HEADER1 = {'trainer_token' : '5d11d92de68b0091ee5af0a2450ccc56'}
HEADER2 = {'Content-Type': 'application/json'}
HEADERS = {**HEADER1, **HEADER2}

def test_ststus_code ():
  respons = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 154})
  assert respons.status_code == 200

def test_part_of ():
  respons = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 154})
  assert respons.json()['data'][0]['trainer_name'] == 'Щддды'
