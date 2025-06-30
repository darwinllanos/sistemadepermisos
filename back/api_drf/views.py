from rest_framework import viewsets
from .models import (
    vEmployeeAutorizado,
    vPayRollAutorizado,
    TypePayment,
    Month
)
from .serializers import (
    EmployeeSerializer,
    PayRollSerializer,
    TypePaymentSerializer,
    MonthSerializer
)

class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = vEmployeeAutorizado.objects.all()
    serializer_class = EmployeeSerializer

class PayRollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = vPayRollAutorizado.objects.all()
    serializer_class = PayRollSerializer

class TypePaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypePayment.objects.all()
    serializer_class = TypePaymentSerializer

class MonthViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
