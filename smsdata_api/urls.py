from django.urls import path
from .views import SmsDataListCreate, SmsDataRUD

app_name = 'smsdata_api'

urlpatterns = [
    path('', SmsDataListCreate.as_view(), name='SmsDataListCreate'),  # <email>/
    path('rud/<id>/', SmsDataRUD.as_view(), name='SmsDataRUD'),
]
