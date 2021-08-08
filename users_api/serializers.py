from rest_framework import serializers
from users_api.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__'

    def create(self, validated_data):
        '''
        on create this function is running
        for hashing passwords
        for sending email
        '''
        password = validated_data.pop('password')
        user = User(email=validated_data['email'])  # username
        user.set_password(password)
        user.is_active = False
        user.save()

        ################# SEND EMAIL ####################
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        domain = get_current_site(self.context['request']).domain  # self.context['request'] instead of self.request
        link = reverse('users_api:activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

        email_subject = 'فعال سازی اکانت'

        activate_url = f'http://{domain}{link}'

        email_body = '''سلام {}
                برای فعال سازی اکانت خود روی لینک زیر کلیک کنید
                {}'''.format(user.username, activate_url)

        to_email = validated_data['email']
        email = EmailMessage(
            email_subject, email_body, 'noreply@semycolon.com', [to_email],
        )
        email.send(fail_silently=False)
        ################# SEND EMAIL ####################

        return user
