# Generated by Django 4.0.6 on 2022-07-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['-artist']},
        ),
    ]