from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient, Instruction, RecipeRating
from kitchenRecipes.forms import CategoryForm, DifficultyLevelForm, RecipesForm, IngredientForm, InstructionForm, RecipeRatingForm
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

class InstructionListView(ListView):
    model = Instruction
    template_name = 'instruction_list.html'
    context_object_name = 'instructions'

class InstructionDetailView(DetailView):
    model = Instruction
    template_name = 'instruction_detail.html'
    context_object_name = 'instruction'

@login_required
def add_instruction(request):
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instruction_list')
    else:
        form = InstructionForm()
    return render(request, 'instruction_form.html', {'form': form})

@login_required
def edit_instruction(request, pk):
    instruction = get_object_or_404(Instruction, pk=pk)
    if request.method == 'POST':
        form = InstructionForm(request.POST, instance=instruction)
        if form.is_valid():
            form.save()
            return redirect('instruction_list')
    else:
        form = InstructionForm(instance=instruction)
    return render(request, 'instruction_form.html', {'form': form})

@login_required
def delete_instruction(request, pk):
    instruction = get_object_or_404(Instruction, pk=pk)
    if request.method == 'POST':
        instruction.delete()
        return redirect('instruction_list')
    return render(request, 'instruction_confirm_delete.html', {'instruction': instruction})

class RecipeRatingListView(ListView):
    model = RecipeRating
    template_name = 'recipe_rating_list.html'
    context_object_name = 'recipe_ratings'

class RecipeRatingDetailView(DetailView):
    model = RecipeRating
    template_name = 'recipe_rating_detail.html'
    context_object_name = 'recipe_rating'

@login_required
def add_recipe_rating(request):
    if request.method == 'POST':
        form = RecipeRatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_rating_list')
    else:
        form = RecipeRatingForm()
    return render(request, 'recipe_rating_form.html', {'form': form})

@login_required
def edit_recipe_rating(request, pk):
    recipe_rating = get_object_or_404(RecipeRating, pk=pk)
    if request.method == 'POST':
        form = RecipeRatingForm(request.POST, instance=recipe_rating)
        if form.is_valid():
            form.save()
            return redirect('recipe_rating_list')
    else:
        form = RecipeRatingForm(instance=recipe_rating)
    return render(request, 'recipe_rating_form.html', {'form': form})

@login_required
def delete_recipe_rating(request, pk):
    recipe_rating = get_object_or_404(RecipeRating, pk=pk)
    if request.method == 'POST':
        recipe_rating.delete()
        return redirect('recipe_rating_list')
    return render(request, 'recipe_rating_confirm_delete.html', {'recipe_rating': recipe_rating})