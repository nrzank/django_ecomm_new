from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import generics


from authorization.serializers import UserRegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)


