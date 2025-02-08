from django.contrib import admin

from .forms import StaffForm
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = "name position email phone_number".split()

    form = StaffForm
    fieldsets = (
        (None, {"fields": ("name", "position", "img", )}),
        ("Контакты", {"fields": ("phone_number", "email")}),
    )


