from django.shortcuts import render
from . import models

def homepage(request):
    context = {'homepage': models.Categories.objects.all()}
    return render(request, 'homepage/homepage.html', context)
