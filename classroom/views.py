from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    DetailView
)
from .forms import ClassCreationForm
from .models import Class


@login_required
def home(request):
    context = {
        'class_list': Class.objects.all(),
        'page_title': 'Classes'
    }
    return render(request, 'classroom/home.html', context)


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassDetailView(DetailView):
    model = Class