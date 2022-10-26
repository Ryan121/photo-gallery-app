from django.contrib import admin
from . models import Master_Category, Photo, Person 

# Register your models here.
admin.site.register(Master_Category)
admin.site.register(Photo)
admin.site.register(Person)