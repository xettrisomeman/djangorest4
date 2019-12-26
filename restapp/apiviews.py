from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_class = (IsAuthenticated ,)



