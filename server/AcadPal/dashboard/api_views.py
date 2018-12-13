from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student, Teacher


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
