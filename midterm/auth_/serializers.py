from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth import authenticate

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=28,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('An email address is required to login')
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('A user this email and password not found')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated')

        return {
            'token': user.token,
        }
