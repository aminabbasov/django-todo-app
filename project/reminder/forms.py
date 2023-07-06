from django import forms
from django.forms import ModelForm, Textarea, Select, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import ReminderModel


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    username = forms.CharField(
        label='Username',
        widget=TextInput(
            attrs={
                'class': "form-control",
                'id': "InputUsername",
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        help_text='You can enter any password. There is no validation.',
        widget=PasswordInput(
            attrs={
                'class': "form-control",
                'id': "InputPassword1",
                'aria-describedby': "Password1Help",
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        help_text='Confirm password',
        widget=PasswordInput(
            attrs={
                'class': "form-control",
                'id': "InputPassword2",
                'aria-describedby': "Password2Help",
            }
        )
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'captcha']


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Username',
        widget=TextInput(
            attrs={
                'class': "form-control",
                'id': "InputUsername",
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=PasswordInput(
            attrs={
                'class': "form-control",
                'id': "InputPassword",
            }
        )
    )
    captcha = CaptchaField()


class ReminderForm(ModelForm):

    class Meta:
        model = ReminderModel
        fields = ['title', 'selected_color']
        widgets = {
            'title': Textarea(attrs={
                'class': "form-control",
                'type': "text",
                'placeholder': 'Write a task...',
                'aria-label': "Write your task",
                'rows': "14",
                'style': 'resize: none;',
                }
            ),
            'selected_color': Select(attrs={
                'class': "btn btn-secondary dropdown-toggle",
                'type': "button",
                'data-bs-toggle': "dropdown", 
                'form': "myform",
                }
            ),
        }
