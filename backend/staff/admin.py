from django.contrib import admin

from .forms import StaffCustomForm
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    form = StaffCustomForm
    list_display = ("name", "position")
    search_fields = "name position email phone_number".split()

    fieldsets = (
        (None, {"fields": ("name", "position", "img", )}),
        ("Контакты", {"fields": ("phone_number", "email")}),
    )


