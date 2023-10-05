from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient, Instruction, RecipeRating
from kitchenRecipes.forms import CategoryForm, DifficultyLevelForm, RecipesForm, IngredientForm, InstructionForm, RecipeRatingForm

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

class RecipesListView(ListView):
    model = Recipes
    template_name = 'recipes_list.html'
    context_object_name = 'recipes'

class RecipesDetailView(DetailView):
    model = Recipes
    template_name = 'recipes_detail.html'
    context_object_name = 'recipe'

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipesForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipesForm()
    return render(request, 'recipe_form.html', {'form': form})

