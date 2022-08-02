
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView 
from django.core import serializers

from .models import Category, Fact
import json


# Here View is the base view class to handle render
# ContextMixin is to deal with context

class FactsMainPageView(View):

    categories = Category.objects.all()
    template_name = 'facts_templates/1_facts_main_page.html'
    def get(self, request, *args, **kwargs):
        context={'categories':self.categories}
    
      
        return render(request, self.template_name, context=context)


class FactsGetFact(View):
    template_name = 'facts_templates/1_facts_main_page.html'
    queryset = Fact.objects.all()

    def get(self, request, *args, **kwargs):

        category = kwargs['category']


