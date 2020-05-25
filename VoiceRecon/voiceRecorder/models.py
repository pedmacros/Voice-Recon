from django.db import models


# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=120)
