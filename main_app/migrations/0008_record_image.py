# Generated by Django 4.0.6 on 2022-07-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_record_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]