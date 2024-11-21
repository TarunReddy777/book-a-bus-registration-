from django.contrib import admin
from .models import Bus, BusCompany, Seat, Route, Driver

# Register your models here
admin.site.register(Bus)
admin.site.register(BusCompany)
admin.site.register(Seat)
admin.site.register(Route)
admin.site.register(Driver)

