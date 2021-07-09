from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from .forms import EditMember
from .models import Class
from database_function.conversion import get_all_class_member, convert_member, create_member_query, convert_to_usable_value
from database_function.home_view import get_available_class_student, get_available_class_ta, get_available_class_teacher, check_status


@login_required
def home(request):
    class_as_student = get_available_class_student(request.user.id)
    class_as_ta = get_available_class_ta(request.user.id)
    class_as_teacher = get_available_class_teacher(request.user.id)
    only_student = False
    no_class = False
    if check_status(request.user.id) == 1:
        only_student = True
    elif check_status(request.user.id) == 2:
        no_class = True
    context = {
        'class_as_student': class_as_student,
        'class_as_ta': class_as_ta,
        'class_as_teacher': class_as_teacher,
        'only_student': only_student,
        'no_class': no_class,
        'page_title': 'Classes',
    }
    return render(request, 'classroom/home.html', context)


@login_required
def view_member(request, pk):
    class_detail = get_object_or_404(Class, pk=pk)
    student, ta, teacher = convert_to_usable_value(class_detail)
    context = {
        'page_title': 'Member',
        'class': class_detail,
        'student': student,
        'ta': ta,
        'teacher': teacher,
        'student_number': len(student),
        'ta_number': len(ta),
        'teacher_number': len(teacher),
    }
    return render(request, 'classroom/class_member.html', context)


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.teacher = self.request.user.id
        return super().form_valid(form)


class ClassDetailView(DetailView):
    model = Class


class ClassUpdateMember(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    template_name = 'classroom/class_editmember.html'
    fields = ['student', 'ta', 'teacher']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'classroom/class_delete.html'
    success_url = '/'
