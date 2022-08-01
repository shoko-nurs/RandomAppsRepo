from email import contentmanager
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic.base import View, ContextMixin
from django.shortcuts import render



# Here View is the base view class to handle render
# ContextMixin is to deal with context

class FactsMainPageView(View,ContextMixin):
    template_name = 'facts_templates/1_facts_main_page.html'
    
    def get(self, request, *args, **kwargs):

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['test_info'] = 123
            return context

        return render(request, self.template_name)