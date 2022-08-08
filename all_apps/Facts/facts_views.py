from email import contentmanager
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Fact
from django.conf import settings

class FactsMainPageView(View):

    categories = Category.objects.all()
    template_name = 'facts_templates/1_facts_main_page.html'

    def get(self, request, *args, **kwargs):
        context={'categories':self.categories}
    
        return render(request, self.template_name, context=context)



class UserFactsPage(View):

    def get(self, request, *args, **kwargs):
        context = {'api_key_fetch':settings.API_KEY_FETCH}
        return render(request, 'facts_templates/2_user_facts_page.html', context )