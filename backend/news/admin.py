from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from jet.admin import CompactInline
from .models import News, NewsImage


class NewsImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        if not any(form.cleaned_data and not form.cleaned_data.get("DELETE", False) for form in self.forms):
            raise ValidationError("У новости должно быть хотя бы одно изображение.")



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
