from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('debt_list/', views.debt_list, name='debt_list'),
    path('debt/<int:debt_id>/select_method/', views.select_payment_method, name='select_payment_method'),
    path('calculate_payments/<int:debt_id>/', views.calculate_payments, name='calculate_payments'),
    path('add_debt/', views.add_debt, name='add_debt'),
]