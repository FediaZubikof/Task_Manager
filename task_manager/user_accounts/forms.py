from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control Roboto'}), )
    password2 = forms.CharField(label='Confirm Password (again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control Roboto'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control Roboto'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control Roboto'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control Roboto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control Roboto'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control Roboto'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': "current-password", 'class': 'form-control Roboto'}))
