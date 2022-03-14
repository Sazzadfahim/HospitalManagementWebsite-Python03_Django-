from django.contrib import admin
from .models import information
from .models import hospital


# Register your models here.



admin.site.register(hospital)
admin.site.register(information)

