# Generated by Django 3.2.5 on 2021-07-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='image',
            field=models.ImageField(default='default_classroom.jpeg', upload_to='profile_pics'),
        ),
    ]
