# Generated by Django 2.2 on 2020-11-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_student_dojo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='visited',
            field=models.ManyToManyField(related_name='visited_by', to='first_app.Dojo'),
        ),
    ]
