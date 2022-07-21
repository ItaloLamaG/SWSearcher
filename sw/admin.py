from django.contrib import admin
from sw.models.models import (
    People,
    Film,
    Planet,
    Starship,
    Vehicle,
    Species,
    Historic,
)

admin.site.register(People)
admin.site.register(Film)
admin.site.register(Planet)
admin.site.register(Starship)
admin.site.register(Vehicle)
admin.site.register(Species)
admin.site.register(Historic)
