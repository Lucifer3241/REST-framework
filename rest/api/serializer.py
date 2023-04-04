from rest_framework import serializers
from .models import Airport

class AirportSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields=('__all__')
        