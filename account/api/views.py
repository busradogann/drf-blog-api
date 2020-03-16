from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers import UserSerializer, ChangePasswordSerializer, RegisterSerializer
from account.api.permissions import NotAuthenticated
from account.api.throttles import RegisterThrottle


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    #Normalde Update ya da Retrieve APIView'larinda lookup_field verilmediginde hata veriyordu.
    #get_objects methodu ile lookup_field kullanilmadan update ve retrieve islemlerini yapacagiz.

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    # #giris yapmis kullanicinin bilgilerini dondurur
    # def get_object(self):
    #     return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.request.user

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({"old_password": "wrong password"}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(CreateAPIView):
    throttle_classes = [RegisterThrottle]
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]
