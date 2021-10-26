from django.contrib import admin
from .models import (Counties,
Mushroom,
MushroomCondition)

# Register your models here.
admin.site.register(Counties)
admin.site.register(Mushroom)
admin.site.register(MushroomCondition)
