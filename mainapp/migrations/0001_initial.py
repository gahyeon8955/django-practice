# Generated by Django 3.2.4 on 2021-08-22 10:37

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to=mainapp.models.Blog.date_upload_to)),
            ],
        ),
    ]
