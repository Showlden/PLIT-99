from django import forms
from .models import BaseStudyModel


class StudyForm(forms.ModelForm):
    class Meta:
        model = BaseStudyModel
        fields = "__all__"
        labels = {
            "preview_img": "Предварительное изображение",
            "banner_img": "Основное изображение",
        }