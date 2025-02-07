from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User




class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
    )

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        else:
            user.password = User.objects.get(id=user.id).password

        if commit:
            user.save()
        return user

