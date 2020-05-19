from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	department = models.CharField(max_length=200, default='computer_science')
	description = models.TextField()
	
	def __str__(self):
		"""A string representation of the model."""
		return self.title

