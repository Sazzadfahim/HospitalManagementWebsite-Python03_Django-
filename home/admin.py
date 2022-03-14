from django.contrib import admin
from .models import oxygensupply
from .models import records
from .models import doctor
from .models import user_profile

# Register your models here.


admin.site.register(oxygensupply)
admin.site.register(records)
admin.site.register(doctor)
admin.site.register(user_profile)