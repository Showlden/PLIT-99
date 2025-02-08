from cloudinary.models import CloudinaryField
from django.db import models

class Specialization(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name="Название")
    description = models.TextField(max_length=500, blank=False, null=False, verbose_name="Описание")
    term = models.PositiveIntegerField(default=2, help_text="Срок обучения в годах", verbose_name="Срок обучения")
    contract = models.PositiveIntegerField(default=50000, verbose_name="Обучение на контрактной основе")
    preview_img = CloudinaryField("image")
    banner_img = CloudinaryField("image")

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

class Course(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name="Название")
    description = models.TextField(max_length=500, blank=False, null=False, verbose_name="Описание")
    term = models.PositiveIntegerField(default=2, help_text="Срок обучения в месяцах", verbose_name="Срок обучения")
    price = models.PositiveIntegerField(verbose_name="Цена")
    preview_img = CloudinaryField("image")
    banner_img = CloudinaryField("image")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"