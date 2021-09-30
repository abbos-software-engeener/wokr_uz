from django.contrib import admin
from .models import *

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass