from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели электронную почту')
        if not username:
            raise ValueError('Вы не ввели имя пользователя')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class MyUser(AbstractUser):
    surname = models.CharField(max_length=250)
    place_burn = models.TextField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    books = models.ForeignKey('Books', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.username

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]


class Books(models.Model):
    name_book = models.CharField(max_length=250, unique=True)
    author_name = models.CharField(max_length=200)
    year_written = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.name_book
