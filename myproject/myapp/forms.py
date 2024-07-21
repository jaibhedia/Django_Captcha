from django import forms
from captcha.fields import CaptchaField
from .models import User

class RegistrationForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
