from django.shortcuts import render
from rest_framework import generics
from api.serializers import TechCustomSerializer, PersonSerializer
from technologies.models import Technologie
from persons.models import PersonTech, Person


class MyView(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
