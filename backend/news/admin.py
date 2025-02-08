from django.contrib import admin

from .models import News, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 5

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    search_fields = "title description date type".split()

    inlines = [NewsImageInline]