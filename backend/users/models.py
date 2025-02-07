from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin, Group, Permission,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .managers import CustomUserManager

POSITION = [
    ('Главный администратор', 'Главный администратор'),
    ('Администратор', 'Администратор'),
]

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=24, unique=True, verbose_name="Имя пользователя (на английском)")
    position = models.CharField(choices=POSITION, default="Администратор", blank=False, null=False, max_length=21)
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    is_staff = models.BooleanField(default=False, verbose_name="Администратор")
    is_superuser = models.BooleanField(default=False, verbose_name="Главный администратор")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.position == "Главный администратор":
            self.is_superuser = True
            self.is_staff = True
        elif self.position == "Администратор":
            self.is_superuser = False
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        super().save(*args, **kwargs)

        staff_group, created = Group.objects.get_or_create(name="staff")

        if created:
            custom_models = ContentType.objects.filter(
                app_label__in=["staff", "news"])
            for content_type in custom_models:
                permissions = Permission.objects.filter(content_type=content_type)
                staff_group.permissions.add(*permissions)

        if self.position == "Администратор":
            self.groups.set([staff_group])
        else:
            self.groups.clear()
