from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import SmsDataSerializer
from .models import SmsData
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

# Create your views here.


class SmsDataListCreate(ListCreateAPIView):
    '''
    list create
    '''
    queryset = SmsData.objects.all()
    serializer_class = SmsDataSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['user__email']


class SmsDataRUD(RetrieveUpdateDestroyAPIView):
    queryset = SmsData.objects.all()
    serializer_class = SmsDataSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['id']
    lookup_field = 'id'
