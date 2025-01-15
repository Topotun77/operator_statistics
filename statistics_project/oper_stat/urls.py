from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('', views.report_all, name='report_all'),
    path('form/', views.report_form, name='report_form'),
    path('<str:pk>/', views.report_oper, name='report_oper'),
]

