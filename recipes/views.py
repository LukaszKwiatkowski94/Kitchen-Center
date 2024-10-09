from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import *


def index(request):
    return render(request, 'index.htm')

def get(request):
    return HttpResponse("Get recipe by id: "+request.recipe)


