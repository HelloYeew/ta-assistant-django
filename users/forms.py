from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Config, CODE_HIGHLIGHT


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    student_id = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['student_id', 'image']


class UserConfigGeneralForm(forms.ModelForm):
    code_highlight = forms.CharField(label='Code Highlight Color', widget=forms.Select(choices=CODE_HIGHLIGHT))

    class Meta:
        model = Config
        fields = ['code_highlight']
