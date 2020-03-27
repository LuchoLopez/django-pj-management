from django.db import models
from technologies.models import Technologie
# Create your models here.


class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    technologies = models.ManyToManyField(Technologie, through='PersonTech', related_name='persons')

    def __str__(self):
        return self.name


class PersonTech(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    technologie = models.ForeignKey(Technologie, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return "%s -> %s (%s)" % (self.person, self.technologie, self.level)
