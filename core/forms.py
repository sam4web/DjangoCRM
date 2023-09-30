from django import forms
from django.forms import ModelForm
from core.models import Record


INPUT_CLASSES = "border-2 border-slate-700 rounded-md px-4 py-3 text-lg w-full"


class RecordForm(ModelForm):
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
