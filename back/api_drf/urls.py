from rest_framework import routers
from .views import (
    EmployeeViewSet,
    PayRollViewSet,
    TypePaymentViewSet,
    MonthViewSet
)

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'payrolls', PayRollViewSet, basename='payrolls')
router.register(r'typepayments', TypePaymentViewSet, basename='typepayments')
router.register(r'months', MonthViewSet, basename='months')

urlpatterns = router.urls

