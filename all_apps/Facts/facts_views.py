
from re import template
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Fact



# Here View is the base view class to handle render
# ContextMixin is to deal with context

class FactsMainPageView(View):
    
    template_name = 'facts_templates/1_facts_main_page.html'
    categories = Category.objects.all()
    facts = Fact.objects.all()

    def get(self, request, *args, **kwargs):
        
        context = { 
                        "categories":self.categories,
                        "facts":self.facts
                        }

        return render(request, self.template_name, context)


class FactsGetFact(View):
    template_name = 'facts_templates/1_facts_main_page.html'
    categories = Category.objects.all()
    facts = Fact.objects.all()

    def get(self, request, *args, **kwargs):

        category = kwargs['category']

