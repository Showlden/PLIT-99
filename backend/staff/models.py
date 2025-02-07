from cloudinary.models import CloudinaryField
from django.db import models

POSITION = [
    ('Мастер П/О', 'Мастер П/О'),
    ('Преподователь', 'Преподователь'),
    ('Учебная часть', 'Учебная часть'),
    ('Директор', 'Директор'),
    ('Заместитель директора', 'Заместитель директора'),
]

class Staff(models.Model):
    name = models.CharField(max_length=54, blank=False, null=False, verbose_name="Имя")
    position = models.CharField(choices=POSITION, default="Преподователь", blank=False, null=False, max_length=21, verbose_name="Должность")
    img = CloudinaryField("image")
    phone_number = models.CharField(max_length=13, blank=False, null=False, verbose_name="Номер телефона")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Почта")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name