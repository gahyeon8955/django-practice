# Generated by Django 3.2.4 on 2021-08-13 07:24

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to=mainapp.models.Blog.date_upload_to),
        ),
    ]