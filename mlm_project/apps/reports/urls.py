from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_preview, name='report_preview'),
    path('pdf/', views.export_pdf, name='export_pdf'),
]
