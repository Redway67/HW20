import requests
import pprint

# hotelier
token = 'a2d14d2ec65b19920c1f2df65416090297a4978e'
headers = {'Authorization': f'Token {token}'}
# Гостей может просматривать только администратор гостиницы
response = requests.get('http://127.0.0.1:8000/api/v0/clients/', headers=headers)
pprint.pprint(response.json())


