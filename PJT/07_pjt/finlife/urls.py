from django.urls import path
from . import views

app_name = 'finlife'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name = 'save-deposit-products'),
    path('deposit-products/', views.deposit_products, name = 'deposit-products'),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options, name = 'deposit-products-options'),
    path('deposit-products/top_rate/', views.top_rate, name = 'top_rate'),
    # path('api-test/', views.api_test, name = 'api_test'),
]