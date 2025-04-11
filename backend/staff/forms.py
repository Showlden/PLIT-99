from django import forms
from django.core.exceptions import ValidationError

from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        labels = {
            "img": "Изображение"
        }

    def clean_img(self):
        img = self.cleaned_data.get("img")
        if img and hasattr(img.file, "content_type"):
            if not img.file.content_type.startswith("image"):
                raise ValidationError("Файл должен быть изображением.")
        return img
