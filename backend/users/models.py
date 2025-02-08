from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .managers import CustomUserManager

POSITION_CHOICES = [
    ('Главный администратор', 'Главный администратор'),
    ('Администратор', 'Администратор'),
]

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=24, unique=True, verbose_name="Имя пользователя (на английском)")
    position = models.CharField(choices=POSITION_CHOICES, default="Администратор", blank=False, null=False, max_length=21)
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
        self.is_superuser = self.position == "Главный администратор"
        self.is_staff = self.position in ["Главный администратор", "Администратор"]

        super().save(*args, **kwargs)

        staff_group, created = Group.objects.get_or_create(name="staff")

        if created:
            custom_models = ContentType.objects.filter(app_label__in=["staff", "news", "study"])
            permissions = Permission.objects.filter(content_type__in=custom_models)
            staff_group.permissions.add(*permissions)

        if self.position == "Администратор":
            self.groups.add(staff_group)
        else:
            self.groups.remove(staff_group)