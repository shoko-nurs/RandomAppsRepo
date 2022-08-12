from logging import raiseExceptions
from pydoc import resolve
from urllib import response
import requests


# ######### Get all categories ###########
def GetAllCategories(user):
    if user==1:

        url = 'http://127.0.0.1:8000/facts/api/all_categories?api_key=123456'
    else:
        url = 'http://127.0.0.1:8000/facts/api/all_categories?api_key=qwerty'
    response = requests.get(url)


    response = response.json()

    print(response)
    print(len(response))



####### Get 1 category ################
def GetCategory(user):
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=123456'

    else:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=qwerty'
    response = requests.get(url)
    print(response.json())


def EditCategory(user):
    
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=123456'

    else:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=qwerty'
    response = requests.put(url)
    print(response.json())


user=2
GetAllCategories(user)
GetCategory(user)
# EditCategory(user)