from django.urls import path
from . import views

urlpatterns = [
    path('', views.wallet_overview, name='wallet_overview'),
    path('transfer/', views.transfer_wallet, name='transfer_wallet'),
    path('history/', views.wallet_history, name='wallet_history'),
]
