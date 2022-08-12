from logging import raiseExceptions
from pydoc import resolve
from urllib import response
import requests



url = 'http://127.0.0.1:8000/facts/api/get_categories?api_key=123456'

response = requests.get(url)


response = response.json()

print(response)
print(len(response))