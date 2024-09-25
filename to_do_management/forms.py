from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from to_do_management.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"