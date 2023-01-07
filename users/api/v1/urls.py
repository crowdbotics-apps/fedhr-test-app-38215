
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EmployeeViewSet
router = DefaultRouter()
router.register('employee', EmployeeViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
