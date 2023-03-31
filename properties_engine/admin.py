from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(PgFacility)
admin.site.register(LatestPg)
admin.site.register(PgType)
admin.site.register(LatesFlat)

