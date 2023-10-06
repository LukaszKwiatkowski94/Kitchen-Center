from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient
from kitchenRecipes.forms import CategoryForm, DifficultyLevelForm, RecipesForm, IngredientForm
from django.contrib.auth.decorators import login_required

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

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

class DifficultyLevelListView(ListView):
    model = DifficultyLevel
    template_name = 'difficulty_level_list.html'
    context_object_name = 'difficulty_levels'

class DifficultyLevelDetailView(DetailView):
    model = DifficultyLevel
    template_name = 'difficulty_level_detail.html'
    context_object_name = 'difficulty_level'

@login_required
def add_difficulty_level(request):
    if request.method == 'POST':
        form = DifficultyLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('difficulty_level_list')
    else:
        form = DifficultyLevelForm()
    return render(request, 'difficulty_level_form.html', {'form': form})

@login_required
def edit_difficulty_level(request, pk):
    difficulty_level = get_object_or_404(DifficultyLevel, pk=pk)
    if request.method == 'POST':
        form = DifficultyLevelForm(request.POST, instance=difficulty_level)
        if form.is_valid():
            form.save()
            return redirect('difficulty_level_list')
    else:
        form = DifficultyLevelForm(instance=difficulty_level)
    return render(request, 'difficulty_level_form.html', {'form': form})

@login_required
def delete_difficulty_level(request, pk):
    difficulty_level = get_object_or_404(DifficultyLevel, pk=pk)
    if request.method == 'POST':
        difficulty_level.delete()
        return redirect('difficulty_level_list')
    return render(request, 'difficulty_level_confirm_delete.html', {'difficulty_level': difficulty_level})

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
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipesForm()
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipesForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient_detail.html'
    context_object_name = 'ingredient'

@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient_form.html', {'form': form})

@login_required
def edit_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient_form.html', {'form': form})

@login_required
def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient_confirm_delete.html', {'ingredient': ingredient})
