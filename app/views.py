from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def recipes(request):
    return render(request, 'recipes.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
