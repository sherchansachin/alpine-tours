# Generated by Django 3.2.5 on 2021-07-26 08:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_title', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('days', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='package_images')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=0)),
            ],
        ),
    ]
