from django.db import models


class Technologie(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)

    def __str__(self):
        return self.name
#Technologie.objects.first().persontech_set.all()