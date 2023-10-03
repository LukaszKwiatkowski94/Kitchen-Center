from django.db import models
# from django.contrib.auth.models import User
import datetime

class Category(models.Model):
	categoryName = models.CharField(max_length=150, verbose_name="Category Name")
	
	def __unicode__(self):
		return self.categoryName
	
	def __str__(self):
		return self.categoryName
	
class Recipes(models.Model):
	name = models.CharField(max_length=500, verbose_name="Name")
	description = models.TextField(blank=True, verbose_name="Description")
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	createAt = models.DateTimeField(default=datetime.datetime.now,verbose_name="Date of create")
	image = models.FileField(upload_to='recipesImages/', verbose_name="Image")
	published = models.BooleanField(default=False,verbose_name="Published")
	# author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
	    return '['+self.id+'] '+self.name