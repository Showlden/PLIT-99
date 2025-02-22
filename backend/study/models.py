from django.db import models
from cloudinary.models import CloudinaryField

class BaseStudyModel(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name="Название")
    description = models.TextField(max_length=500, blank=False, null=False, verbose_name="Описание")
    preview_img = CloudinaryField("image")
    banner_img = CloudinaryField("image")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Specialization(BaseStudyModel):
    term = models.PositiveIntegerField(default=2, help_text="Срок обучения в годах", verbose_name="Срок обучения")
    contract = models.PositiveIntegerField(default=50000, verbose_name="Обучение на контрактной основе")

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

class Course(BaseStudyModel):
    term = models.PositiveIntegerField(default=2, help_text="Срок обучения в месяцах", verbose_name="Срок обучения")
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"