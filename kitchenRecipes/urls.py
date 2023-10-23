from django.urls import path
from . import views

app_name = 'kitchenRecipes'

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipe-list')
]
