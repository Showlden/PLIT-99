from django.contrib import admin
from jet.admin import CompactInline

from .models import News, NewsImage

class NewsImageInline(CompactInline):
    model = NewsImage
    extra = 5
    show_change_link = True

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('is_pinned',)
    search_fields = "title description date type is_pinned".split()

    inlines = [NewsImageInline]

    def save_model(self, request, obj, form, change):
        if obj.is_pinned:
            News.objects.exclude(id=obj.id).update(is_pinned=False)
        super().save_model(request, obj, form, change)