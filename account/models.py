from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class MyAccountManager(BaseUserManager):

    # create_user and create_superuser is mandatory

    def create_user(self, username, password=None):
        if not username:
            raise ValueError("username Required!")

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Почта", max_length=100, unique=True, null=True, blank=True,
    )
    username = models.CharField(max_length=60, unique=True)
    phone = PhoneNumberField("Телефон", unique=True, null=True, blank=True)
    first_name = models.CharField("Фамилия", max_length=100, blank=True, null=True)
    last_name = models.CharField("Имя", max_length=100, blank=True, null=True)
    middle_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="Последнее соединение", auto_now=True
    )
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatars/", null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    USERNAME_FIELD = "username"  # values will be identified using email now
    # shouldn't add 'username' here, since it is already in USERNAME_FIELD
    # REQUIRED_FIELDS = ["email"]

    objects = MyAccountManager()

    # these 3 are required methods
    def __str__(
            self,
    ):  # This gets displayed when an object of Account class is called in template
        return self.username  # multiple values can be concatinated like this

    def has_perm(self, perm, obj=None):  # has permission to make changes
        return self.is_admin  # only allowed if admin

    def has_module_perms(self, app_label):  # give permission to module
        return True  # instead of True we can give access to specific position (eg: is_admin, is_staff or both)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
