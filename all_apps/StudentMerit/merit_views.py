from email import header
from urllib import response
from wsgiref import headers
from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render, redirect
import requests as rq
import json
import jwt
from django.conf import settings
from decouple import config


debug = config('DEBUG')



if debug == "False":
    HOST = 'https://shokonurs-student-merit.herokuapp.com'
elif debug == "True":
    HOST = 'http://localhost:8080'


class MeritExplanationView(View):
    

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')

        return render(request, 'merit_templates/1_merit_explanation.html')



class MeritMainPageView(View):

    def get(self, request, *args, **kwargs):
       
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')

        # Get all actions and pass it to the page
        headers={
            "Authorization":"Bearer "+ token,
            
        }
        
        
        url = HOST+"/api/manage_scores"
    
        response = rq.get(url, headers=headers)
 
        context = {
            'main':json.dumps(response.json()),
            'token':token,

        }
      
        return render(request, 'merit_templates/1_merit_main_page.html', context=context)

    
    # def post(self, request, *args, **kwargs):

    #     # We must convert Python object queryDict into standart Json string
    #     data = request.POST
    #     strData = json.dumps(data)
        
    #     # Then we send this Json string with post request
    #     response = rq.post('http://localhost:8080/api/test',data=strData)
        
    #     # Then we get response of the request, and pass it to Django template
    #     new = response.json()
    #     return render(request, 'merit_templates/1_merit_main_page.html', context=new)




class ManageScoresView(View):

    def get(self, request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')


        url = HOST + "/api/get_endpoints"

        response = rq.get(url,
            headers={
                "Authorization":"Bearer "+token,
                
            }
        )

        data = response.json()
        data['token'] = token

        response = render(request, 'merit_templates/4_manage_scores.html', context=data)
        return response

     
class ManageClassesView(View):

    def get(self, request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')
        
        url = HOST+"/api/get_endpoints"

        response = rq.get(url,
            headers={
                "Authorization":"Bearer "+token,
                 
            }
        )
            


        data = response.json()
        data['token'] = token
    
        response = render(request, 'merit_templates/3_manage_classes.html', context=data)
        return response
        

class ManageStudentsView(View):

    def get(self, request, *args, **kwargs):
       
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')

        url = HOST+"/api/get_endpoints"

        response = rq.get(url,
            headers={
                "Authorization":"Bearer "+token,
             
            }
        )

        data = response.json()
        data['token'] = token
       
        return render(request, 'merit_templates/5_manage_students.html', context=data)


class ManageRecordsView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')


        url = HOST+"/api/get_endpoints"
        response = rq.get(url,
            headers={
                "Authorization":"Bearer "+token,
                
            }
        )

        data = response.json()
        data['token'] = token
      
        return render(request, 'merit_templates/6_my_records.html', context=data)




class ViewScoresView(View):

    def get(self, request, *args, **kwargs):
        sid = kwargs.get('id')
        

        if not request.user.is_authenticated:
            return redirect('login')

        token = request.COOKIES.get('jwtkn')
        try: 
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            return redirect('login')

        url = HOST+"/api/get_endpoints"
        response = rq.get(url,
            headers={
                "Authorization":"Bearer "+token,
                
            }
        )

        data = response.json()
        data['token'] = token
        data['student_id'] = sid
       
        return render(request, 'merit_templates/7_view_student_scores.html', context=data)