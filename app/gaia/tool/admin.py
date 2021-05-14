from django.contrib import admin

from .models import Ability
from .models import Tool
from .models import Weapon


admin.site.register(Ability)
admin.site.register(Tool)
admin.site.register(Weapon)
