from django.urls import path, include
from . import views

urlpatterns = [
    path('a/', views.a),
    path('b/', views.b),
    path('c/', views.c),
]
