from django.db import models


# Create your models here.
class Recording(models.Model):
    author = models.CharField(max_length=120)
