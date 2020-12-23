from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def save(self):
        User.objects.create_user(username=self['username'].value(), password=self['password'].value())
