from rest_framework import authentication
from users.models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Employee.objects.all()