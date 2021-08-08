from django.http import HttpResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from users_api.serializers import UserSerializer
from users_api.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

class TokenDelete(APIView):
    def delete(self, request):
        request.auth.delete()
        return Response(status=204)


class UserCreate(CreateAPIView):
    '''
    create
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRUD(RetrieveUpdateDestroyAPIView):
    '''
    read update delete
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'


class VerificationView(View):
    '''
    for verification email address
    '''

    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if user.is_active:
                return HttpResponse('<h1 style="direction: rtl;">!اکانت شما فعال است</h1>')
            user.is_active = True
            user.save()
            return HttpResponse('<h1 style="direction: rtl;">اکانت شما فعال شد!</h1>')
        except:
            return HttpResponse('<h1 style="direction: rtl;">مشکلی به وجود آمده. لطفا دوباره تلاش کنید.</h1>')
