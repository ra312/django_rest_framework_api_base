# api/views.py
from rest_framework import generics

from employees import models
from . import serializers


class ListEmployee(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class DetailEmployee(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
