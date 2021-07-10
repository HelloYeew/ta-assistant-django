from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Class(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_classroom.png', upload_to='class_pics')
    student = models.CharField(max_length=100000, default=0)
    ta = models.CharField(max_length=100000, default=0)
    teacher = models.CharField(max_length=100000, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class-detail', kwargs={'pk': self.id})