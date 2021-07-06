from django import forms
from .models import Class
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ClassCreationForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ['name', 'image']