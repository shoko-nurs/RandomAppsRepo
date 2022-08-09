from email import contentmanager
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Fact
from django.conf import settings


class FactsMainPageView(View):

    def get(self, request, *args, **kwargs):
        context={'categories':Category.objects.all().filter(user_added=1)}
    
        return render(request, 'facts_templates/1_facts_main_page.html', context=context)



class UserFactsPage(View):

    def get(self, request, *args, **kwargs):
        context = {'api_key_fetch':settings.API_KEY_FETCH}
        return render(request, 'facts_templates/2_user_facts_page.html', context )