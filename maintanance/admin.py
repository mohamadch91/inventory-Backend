from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(maintanance)
admin.site.register(activeMaintance)
admin.site.register(maintancegp)
