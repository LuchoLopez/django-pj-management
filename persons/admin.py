from django.contrib import admin
from persons.models import Person, PersonTech


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonTech)
class PersonTechAdmin(admin.ModelAdmin):
    pass
