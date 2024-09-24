from django.contrib import admin

# Register your models here.
from api.models import Country, Region, Zone, Woreda


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Zone)
admin.site.register(Woreda)