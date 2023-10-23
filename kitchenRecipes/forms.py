from django import forms
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient, Instruction, RecipeRating

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']

class DifficultyLevelForm(forms.ModelForm):
    class Meta:
        model = DifficultyLevel
        fields = ['name']

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'description', 'category', 'createAt', 'image', 'published', 'difficulty_level', 'author']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'recipe']

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['order', 'description', 'recipe']

class RecipeRatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['rating']