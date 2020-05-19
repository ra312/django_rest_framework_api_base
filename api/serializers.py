# api/serializers.py
from rest_framework import serializers
from employees import models


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'name',
			'title',
			'department',
			'description',
		)
		model = models.Employee
