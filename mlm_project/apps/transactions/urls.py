from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.deposit, name='fund_deposit'),
    path('withdrawal/', views.withdrawal, name='fund_withdrawal'),
    path('history/', views.fund_history, name='fund_history'),
]
