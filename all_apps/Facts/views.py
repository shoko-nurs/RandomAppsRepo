
from django.shortcuts import render
from django.views.generic.base import View




# Here View is the base view class to handle render
# ContextMixin is to deal with context

class FactsMainPageView(View):
    
    template_name = 'facts_templates/1_facts_main_page.html'
    
    
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)