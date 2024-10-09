from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(default=True,verbose_name="Active")

    def __str__(self):
	    return self.name

class Recipes(models.Model):
    name = models.CharField(max_length=250, verbose_name="Name")
    description = models.TextField(blank=True, verbose_name="Description")
    dateCreated = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date of creation")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, verbose_name="Active")
    photo = models.FileField(upload_to='recipePhoto/', verbose_name="Photo")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return self.name

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="Name")
    count = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Count")
    unit = models.CharField(max_length=20, verbose_name="Unit")

class StepList(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Order")
    step = models.TextField(blank=False, verbose_name="Step")

class Rates(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)], verbose_name="Rate")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name="Description")