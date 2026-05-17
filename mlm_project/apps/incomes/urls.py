from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.income_summary, name='income_summary'),
]
