from django.contrib import admin
from technologies.models import Technologie


@admin.register(Technologie)
class TechAdmin(admin.ModelAdmin):
    pass
