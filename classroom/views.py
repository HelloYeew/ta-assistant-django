from django.shortcuts import render
from .models import Class


def home(request):
    context = {
        'class_list': Class.objects.all()
    }
    return render(request, 'classroom/home.html', context)
