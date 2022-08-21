from django.contrib import admin

from .models import *


# Register your models here.

admin.site.register(relatedFacility)
admin.site.register(Field)
admin.site.register(relatedItemType)
admin.site.register(facilityParam)
admin.site.register(facilityParamDescription)
admin.site.register(itemParam)
admin.site.register(itemParamDescription)
admin.site.register(Facilityvalidation)
admin.site.register(Itemvalidation)