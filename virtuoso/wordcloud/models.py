from django.db import models

# Create your models here

class Value(models.Model):
	value = models.TextField(blank=False)
	description = models.TextField()
	frequency = models.IntegerField(default=0)

