from django.db import models

# Create your models here.


class Today (models.Model):
    no = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
