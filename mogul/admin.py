from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(BookedGate)
admin.site.register(Route)
admin.site.register(Fleet)
