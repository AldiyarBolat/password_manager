from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.base_user import BaseUserManager
from . import constants
from .validators import validate_name, validate_size, validate_extension


class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class MainUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='User')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email address')
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='First name')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Last name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_staff = models.BooleanField(default=False)
    role = models.CharField(choices=constants.USER_ROLES, default=constants.USER_ROLE_CLIENT,
                            max_length=30, verbose_name='Role')

    objects = MainUserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Profile')
    country = models.CharField(blank=True, null=True, max_length=100, verbose_name='Birthday date')
    photo = models.ImageField(upload_to='avatars', validators=[validate_name, validate_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
