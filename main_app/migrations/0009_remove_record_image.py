# Generated by Django 4.0.6 on 2022-07-14 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_record_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='image',
        ),
    ]
