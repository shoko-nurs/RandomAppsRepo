from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Fact


class FactsMainPageView(View):

    categories = Category.objects.all()
    template_name = 'facts_templates/1_facts_main_page.html'

    def get(self, request, *args, **kwargs):
        context={'categories':self.categories}
    
        return render(request, self.template_name, context=context)

class UserFactsPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'facts_templates/2_user_facts_page.html' )