from django.contrib import admin

from .models.pikmins.pikmin import Pikmin
from .models.planets.planet import Planet


admin.site.register(Pikmin)
admin.site.register(Planet)