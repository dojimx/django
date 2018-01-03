from django.db import models

# Create your models here.

class PersonModel (models.Model):
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)