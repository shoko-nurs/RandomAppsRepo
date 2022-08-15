from django.shortcuts import render
from django.views.generic.base import View

def main(request):
    context={'123':123}
    return render(request, 'main_page.html' , context)



class LeaveMessage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'message.html')