from django.db import models

# Create your models here.
from froala_editor.fields import FroalaField
from django.db import models
from core.utils import *

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 200, unique=True, verbose_name='Name')
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ["name"]
	def __str__(self):
		return self.name

class Information(models.Model):
	title = models.CharField(max_length = 300, verbose_name='Title')
	excerpt = models.TextField(verbose_name='Excerpt')
	content = FroalaField(verbose_name='Content')
	image = models.ImageField(upload_to='Posts/', null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Category')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Data Created')
	updated = models.DateTimeField(auto_now=True, verbose_name='Data Updated')
	hashed = models.CharField(max_length=32, blank=True)

	class Meta:
		verbose_name = 'Information'
		verbose_name_plural = 'Informations'
		ordering = ['-created']
		indexes = [
			models.Index(fields=['category']),
			models.Index(fields=['created']),
		]

	def __str__(self):
		return self.title