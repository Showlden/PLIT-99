from django.contrib import admin
from django.forms import BaseInlineFormSet
from rest_framework.exceptions import ValidationError

from .models import News, NewsImage

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import News, NewsImage


class NewsImageInlineFormset(BaseInlineFormSet):
    def clean(self):
        """ Проверка количества изображений при сохранении в админке """
        images_count = len(self.forms) - sum(1 for form in self.forms if form.cleaned_data.get('DELETE', False))
        if images_count < 3 or images_count > 6:
            raise ValidationError("Количество изображений должно быть от 3 до 6.")


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    formset = NewsImageInlineFormset


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    inlines = [NewsImageInline]
