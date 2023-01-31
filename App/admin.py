from django.contrib import admin
from .models import *

# Register your models here.
class Drones_pics(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Drones, Drones_pics)

class Interactions_pics(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Interactions, Interactions_pics)

class Services_pics(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Services, Services_pics)

