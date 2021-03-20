from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from auth_.models import User
from auth_.serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer

class Profile(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.kwargs['user_id'])

    # def get(self, request, *args, **kwargs):
    #     user = get_object_or_404(User, pk = kwargs['user_id'])
    #     serializer_class = ProfileSerializer(user.profile)
    #     return Response(serializer_class.data)

class Registration(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class Login(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)