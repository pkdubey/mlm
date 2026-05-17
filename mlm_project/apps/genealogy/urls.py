from django.urls import path
from . import views

urlpatterns = [
    path('direct/', views.direct_team, name='direct_team'),
    path('level/', views.level_team, name='level_team'),
    path('genealogy/', views.genealogy_tree, name='genealogy_tree'),
    path('whole/', views.whole_tree, name='whole_tree'),
]
