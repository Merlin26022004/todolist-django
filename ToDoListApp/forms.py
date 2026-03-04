from django import forms
from .models import loginForm, Task

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = loginForm
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = loginForm
        fields = ['username', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
