from django.contrib import admin
from .models import User
from .forms import CustomUserChangeForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    list_display = ('username', 'position')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Position', {'fields': ('position', )}),
    )