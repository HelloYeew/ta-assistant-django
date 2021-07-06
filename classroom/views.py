from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Class


@login_required
def home(request):
    context = {
        'class_list': Class.objects.all(),
        'page_title': 'Classes'
    }
    return render(request, 'classroom/home.html', context)
