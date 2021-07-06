from django.db import models
from django.contrib.auth.models import User
from PIL import Image

ROLE = (
    ('student', "STUDENT"),
    ('teacher', "TEACHER")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(max_length=10, choices=ROLE, default='student', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# TODO: Make auto resize picture system