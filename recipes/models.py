from django.db import models
from django.contrib.auth.models import User
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
    photo = models.FileField(upload_to='newsPhoto/', verbose_name="Photo")
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
		return self.name
