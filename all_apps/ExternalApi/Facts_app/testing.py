from urllib import response
import requests


url = 'http://127.0.0.1:8000/api_documentation/facts_api/all_categories/?api_key=NLFHYART'


response = requests.get(url)

print(response.json())