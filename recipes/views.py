from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import *


def index(request):
    context = {
        'recipes':Recipes.objects.all()
    }
    return render(request, 'index.htm',context)

def get(request):
    return HttpResponse("Get recipe by id: "+request.recipe)


