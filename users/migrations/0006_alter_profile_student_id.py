# Generated by Django 3.2.5 on 2021-07-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_id',
            field=models.IntegerField(null=True),
        ),
    ]
