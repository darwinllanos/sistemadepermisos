from rest_framework import serializers
from .models import (
    vEmployeeAutorizado,
    vPayRollAutorizado,
    TypePayment,
    Month
)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = vEmployeeAutorizado
        fields = '__all__'

class PayRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = vPayRollAutorizado
        fields = '__all__'

class TypePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePayment
        fields = '__all__'

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'
