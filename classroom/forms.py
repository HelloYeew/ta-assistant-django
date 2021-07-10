from django import forms
from .models import Class
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class EditMember(forms.ModelForm):
    student = forms.Textarea()
    ta = forms.Textarea()
    teacher = forms.Textarea()

    class Meta:
        model = Class
        fields = ['student', 'ta', 'teacher']


class AddStudent(forms.Form):
    student_list = forms.CharField(label='Student List', max_length=1000)


class AddTA(forms.Form):
    ta_list = forms.CharField(label='TA List', max_length=1000)


class AddTeacher(forms.Form):
    teacher_list = forms.CharField(label='Teacher List', max_length=1000)
