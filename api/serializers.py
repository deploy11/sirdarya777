from .models import *
from rest_framework.serializers import ModelSerializer

class SorovSerializer(ModelSerializer):
    class Meta:
        model = Sorov
        fields = ('__all__')