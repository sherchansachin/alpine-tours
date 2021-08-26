# Generated by Django 3.2.6 on 2021-08-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='activity',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='packages',
            name='difficulty',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='packages',
            name='elevation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='packages',
            name='route',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='packages',
            name='seasons',
            field=models.CharField(default='', max_length=250),
        ),
    ]
