from django import forms
from cloudinary.forms import CloudinaryFileField

from .models import Staff


class StaffCustomForm(forms.ModelForm):
    img = CloudinaryFileField()
    phone_number = forms.CharField(max_length=13, help_text="Формат: +996XXXXXX")

    class Meta:
        model = Staff
        fields = "name position phone_number email img".split()
