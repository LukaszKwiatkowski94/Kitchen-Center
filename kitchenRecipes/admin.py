from django.contrib import admin
from kitchenRecipes.models import Category, DifficultyLevel, Recipes, Ingredient, Instruction, RecipeRating

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName',)

class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author', 'published', 'createAt')
    list_filter = ('category', 'published', 'difficulty_level')
    search_fields = ('name', 'description')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'recipe')
    search_fields = ('name', 'recipe__name')

class InstructionAdmin(admin.ModelAdmin):
    list_display = ('order', 'description', 'recipe')
    search_fields = ('description', 'recipe__name')

class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'rating')
    list_filter = ('rating',)
    search_fields = ('recipe__name', 'user__email')

admin.site.register(Category, CategoryAdmin)
admin.site.register(DifficultyLevel, DifficultyLevelAdmin)
admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Instruction, InstructionAdmin)
admin.site.register(RecipeRating, RecipeRatingAdmin)