from django.urls import path, include
from .views import *

urlpatterns = [
    path('persons', MyView.as_view(), name='persons'),
]
