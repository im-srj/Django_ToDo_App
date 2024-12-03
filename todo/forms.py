from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["completed", "created_at"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Got a task? Add it here!",
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "What’s this task about?",
                    "cols": 80,
                    "rows": 3,
                    "class": "form-control",
                }
            ),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }
