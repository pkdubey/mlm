from django.urls import path
from . import views

urlpatterns = [
    path('', views.support_list, name='support_list'),
    path('create/', views.support_create, name='support_create'),
    path('<int:pk>/', views.support_detail, name='support_detail'),
    path('help/', views.help_center, name='help_center'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_service, name='terms_of_service'),
    path('contact/', views.contact_us, name='contact_us'),
]
