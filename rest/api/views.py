from rest_framework import generics

from .models import Airport
from .serializer import AirportSerilizer


class AirportList(generics.ListCreateAPIView):
    serializer_class=AirportSerilizer
    queryset=Airport.objects.all()

class AirportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=AirportSerilizer
    queryset=Airport.objects.all()
