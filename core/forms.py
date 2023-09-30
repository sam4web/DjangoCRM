from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from core.models import Record


INPUT_CLASSES = "border-2 border-slate-700 rounded-md px-4 py-3 text-lg w-full"


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["name", "email", "city", "state", "zip_code"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter name",
                    "class": INPUT_CLASSES,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter email address",
                    "class": INPUT_CLASSES,
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "placeholder": "Enter city",
                    "class": INPUT_CLASSES,
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "placeholder": "Enter state",
                    "class": INPUT_CLASSES,
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "placeholder": "Enter zip code ",
                    "class": INPUT_CLASSES,
                }
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username", "class": INPUT_CLASSES}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": INPUT_CLASSES}
        )
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter username", "class": INPUT_CLASSES}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter email", "class": INPUT_CLASSES}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": INPUT_CLASSES}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Repeat password", "class": INPUT_CLASSES}
        )
    )
