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




def EditCategory(user):
    
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=123456'

    else:
        url = 'http://127.0.0.1:8000/facts/api/category/cars?api_key=qwerty'
    

    data = {
        'category':"Edited Category"

    }

    response = requests.put(url, data)
    print(response.json())

####### Get 1 category ################
def GetCategory(user):
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/category/36?api_key=123456'

    else:
        url = 'http://127.0.0.1:8000/facts/api/category/sport?api_key=qwerty'
    response = requests.get(url)
    print(response.json())


def CreateCategory(user):
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/create_category/?api_key=123456'
    else:
        url = 'http://127.0.0.1:8000/facts/api/create_category/?api_key=qwerty'

    data = {
            'category':"New  Cat", 
    }

    response = requests.post(url, json=data)
    print(response.json())


def DeleteCategory(user):
    if user==1:
        url = 'http://127.0.0.1:8000/facts/api/create_category/?api_key=123456'
    else:
        url = 'http://127.0.0.1:8000/facts/api/create_category/?api_key=qwerty'

    data = {
            'category':"New  Cat", 
    }


user=2
#GetAllCategories(user)
#GetCategory(user)
EditCategory(user)
# CreateCategory(2)