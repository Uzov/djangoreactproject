from __future__ import unicode_literals
from django.db import (models, transaction)
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email,and password"""
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """"
    An abstract base class implementing a fully featured User model with admin-compliant permissions.
    """
    email = models.EmailField(verbose_name='email', max_length=40, unique=True, blank=False)
    first_name = models.CharField(verbose_name='имя', max_length=30, blank=False)
    last_name = models.CharField(verbose_name='фамилия', max_length=30, blank=False)
    middle_name = models.CharField(verbose_name='отчество', max_length=30, blank=True)
    birthday = models.DateField(verbose_name='дата_рождения', blank=False)
    passport_number = models.CharField(verbose_name='номер_паспорта', max_length=15, blank=True)
    passport_date = models.DateField(verbose_name='дата_паспорта', blank=True, default='1900-01-01')
    phone = models.CharField(verbose_name='телефон', max_length=20, blank=True)
    sex = models.CharField(verbose_name='пол', max_length=10, blank=True)
    citizen = models.CharField(verbose_name='гражданство', max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'is_staff']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
