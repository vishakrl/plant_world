from django.contrib import admin 
from .models import plant 
admin.site.register(plant)
from .models import comment
admin.site.register(comment)

# Register your models here.
