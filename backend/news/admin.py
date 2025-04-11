from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, ModelForm

from jet.admin import CompactInline

from .models import News, NewsImage


class NewsImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_image = False
        allowed_extensions = ["jpg", "jpeg", "png", "gif"]

        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                has_image = True
                image = form.cleaned_data.get("image")

                if not image:
                    raise ValidationError("Изображение обязательно для загрузки.")

                # Проверяем расширение файла
                if hasattr(image, "name"):  # Для загружаемых файлов (InMemoryUploadedFile)
                    ext = image.name.split(".")[-1].lower()
                else:  # Для уже загруженных в Cloudinary файлов
                    ext = image.url.split(".")[-1].lower() if hasattr(image, "url") else ""

                if ext not in allowed_extensions:
                    raise ValidationError("Файл должен быть изображением (jpg, jpeg, png, gif).")

        if not has_image:
            raise ValidationError("У новости должно быть хотя бы одно изображение.")

# class NewsImageForm(ModelForm):
#     def clean_image(self):
#         image = self.cleaned_data.get("image")
#         if image and not image.content_type.startswith("image"):
#             raise ValidationError("Файл должен быть изображением.")
#         return image

class NewsImageInline(CompactInline):
    model = NewsImage
    extra = 5
    show_change_link = True
    formset = NewsImageInlineFormSet


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "type"]
    list_filter = ["is_pinned"]
    search_fields = ["title", "description", "date", "type", "is_pinned"]

    inlines = [NewsImageInline]

    def save_model(self, request, obj, form, change):
        if obj.is_pinned:
            News.objects.exclude(id=obj.id).update(is_pinned=False)
        super().save_model(request, obj, form, change)
