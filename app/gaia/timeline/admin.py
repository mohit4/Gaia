from django.contrib import admin

from .models import Timeline
from .models import Event

admin.site.register(Timeline)
admin.site.register(Event)
