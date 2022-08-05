import requests


url = 'http://127.0.0.1:8000/user/api/registration'


data = {
    'email': 'b@gmail.com',
    'password1': 'nurguldana',
    'password2': 'nurguldana',
    }


response = requests.post(url, data)
print(response.status_code)
print(response.json())