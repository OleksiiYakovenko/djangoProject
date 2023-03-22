from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GeneratedCSV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generatedCSV', null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(GeneratedCSV, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    order = models.CharField(max_length=255)

    def __str__(self):
        return self.name
