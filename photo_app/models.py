from email.mime import image
from django.db import models

# Create your models here.
class Master_Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Master_Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description


class Person(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
