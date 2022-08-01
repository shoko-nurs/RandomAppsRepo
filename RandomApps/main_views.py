from django.shortcuts import render


def main(request):
    context={'123':123}
    return render(request, 'main_page.html' , context)