from django.shortcuts import render
from models import Categories

def homepage(request):
    context = {'homepage': Categories.objects.all()}
    return render(request, 'homepage/homepage.html', context)

def allCategories(request):
    context={"allCategories":Categories.objects.all()}
    return render(request,"homepage/homepage.html",context)
