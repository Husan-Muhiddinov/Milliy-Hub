from django import forms
from .models import CallBack


class SignupForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = '__all__'