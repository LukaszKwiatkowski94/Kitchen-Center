from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

CustomUser = get_user_model()

class Category(models.Model):
	categoryName = models.CharField(max_length=150, verbose_name="Category Name")
	
	def __unicode__(self):
		return self.categoryName
	
	def __str__(self):
		return self.categoryName
      
class DifficultyLevel(models.Model):
    name = models.CharField(max_length=20, verbose_name="Difficulty Level")

    def __str__(self):
        return self.name
	
class Recipes(models.Model):
    name = models.CharField(max_length=500, verbose_name="Name")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createAt = models.DateTimeField(default=datetime.datetime.now,verbose_name="Date of create")
    image = models.FileField(upload_to='recipesImages/', verbose_name="Image")
    published = models.BooleanField(default=False,verbose_name="Published")
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
	    return f'[{self.id}]: {self.name}'

class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ingredient Name")
    quantity = models.CharField(max_length=50, verbose_name="Quantity")
    unit = models.CharField(max_length=20, verbose_name="Unit") 
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f'{self.name} {self.quantity}'
	
class Instruction(models.Model):
    order = models.PositiveIntegerField(verbose_name="Step Order")
    description = models.TextField(verbose_name="Step Description")
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='instructions')

    def __str__(self):
        return f'Step {self.order}: {self.description}'
	
class RecipeRating(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Rating for Recipe {self.recipe.name}: {self.rating}'