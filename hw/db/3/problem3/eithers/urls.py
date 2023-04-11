from django.urls import path
from . import views

app_name = 'eithers'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('random/', views.random, name='random'),
    path('<pk>/', views.detail, name='detail'),
    path('<pk>/update/', views.update, name='update'),
    path('<pk>/delete/', views.delete, name='delete'),
    path('<pk>/comment/', views.comment, name='comment'),
    path('<question_pk>/comment/<comment_pk>/delete', views.comment_delete, name='comment_delete'),
]