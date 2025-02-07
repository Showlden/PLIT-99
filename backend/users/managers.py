from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, position, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели username!")
        if not password:
            raise ValueError("Вы не ввели пароль!")

        user = self.model(
            username=username,
            position=position,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, position="Администратор", password=None, **extra_fields):
        return self._create_user(username, position, password, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(
            username,
            position="Главный администратор",
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
