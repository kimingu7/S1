from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<pk>/', views.complete, name='complete'),
    path('<pk>/delete/', views.delete, name='delete'),
]
