from django.contrib import admin

from .models import Currency
from .models import Resource


admin.site.register(Currency)
admin.site.register(Resource)
