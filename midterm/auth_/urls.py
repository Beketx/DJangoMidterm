from django.urls import  path
from rest_framework.routers import DefaultRouter
from .views import Registration, Login, Profile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'registration', Registration, basename='registration')
router.register('user/<user_id>/', Profile, basename='profile')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
              ] + router.urls
