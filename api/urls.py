
from django.urls import path
from api.views import RandomMathFacts

urlpatterns = [
    path('api/classify-number', RandomMathFacts, name='random_math_facts'),
]
