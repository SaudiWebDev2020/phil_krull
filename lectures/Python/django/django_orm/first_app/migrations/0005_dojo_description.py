# Generated by Django 2.2 on 2020-11-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_student_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
