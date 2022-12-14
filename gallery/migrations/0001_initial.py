# Generated by Django 4.0.5 on 2022-07-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='gallery')),
                ('captions', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('captions', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=255)),
                ('images', models.ManyToManyField(to='gallery.photo')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
