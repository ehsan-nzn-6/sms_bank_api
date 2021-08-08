from django.db import models
from users_api.models import User


class SmsData(models.Model):
    address = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    description = models.CharField(
        max_length=100, null=True, blank=True)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.datetime}'
