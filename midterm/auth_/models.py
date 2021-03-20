from django.db import models
import jwt

from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.ValidationError],
                              unique=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)
    SuperAdmin = 1
    Guest = 2

    ROLE_CHOICES = (
        (SuperAdmin, 'SuperAdmin'),
        (Guest, 'Guest'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def _create_user(self, username, email,
                     password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        ###what is _db
        user.save(using=self._db)

class Profile(models.Model):
    telephone = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
