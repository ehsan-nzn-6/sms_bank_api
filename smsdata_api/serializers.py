from rest_framework import serializers
from .models import SmsData


class SmsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsData
        fields = '__all__'
