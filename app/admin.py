from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)