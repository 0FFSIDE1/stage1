
from django.urls import path
from api.views import NumberView

urlpatterns = [
    path('api/classify-number', NumberView.as_view(), name='random_math_facts'),
]
