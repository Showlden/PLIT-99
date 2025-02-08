from django import forms
from .models import Specialization, Course


class StudyForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = "__all__"
        labels = {
            "preview_img": "Предварительное изображение",
            "banner_img": "Основное изображение",
        }