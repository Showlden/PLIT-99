from django.db import models
from cloudinary.models import CloudinaryField

NEWS_TYPES = [
    ("Новость", "Новость"),
    ("Событие", "Событие"),
    ("Анонс", "Анонс"),
]

class News(models.Model):
    title = models.CharField(max_length=80, blank=False, null=False, verbose_name="Заголовок")
    description = models.TextField(max_length=500, blank=False, null=False, verbose_name="Описание")
    date = models.DateField(verbose_name="Дата", null=False)
    type = models.CharField(choices=NEWS_TYPES, default="Новость", blank=False, null=False, max_length=7, verbose_name="Тип новости")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey('News', related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image {self.image.url}"