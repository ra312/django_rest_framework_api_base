# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListEmployee.as_view()),
    path('<int:pk>/', views.DetailEmployee.as_view()),
]
