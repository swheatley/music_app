from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ['email']
        exclude = ['username']


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserhangeForm, self).__init(*args, **kwargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        exlcude = ['username']


class UserSignUp(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget = forms.PasswordInput())


class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget = forms.PasswordInput())







