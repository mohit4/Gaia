from django.contrib import admin

from .models import Project
from .models import Reference

admin.site.register(Project)
admin.site.register(Reference)