# Generated by Django 3.0.2 on 2020-01-26 12:15

from django.db import migrations, models
import verification.models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0003_auto_20200125_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='chromosome_22',
        ),
        migrations.RemoveField(
            model_name='image',
            name='chromosome_9',
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_22a',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('22a')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_22b',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('22b')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_9a',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('9a')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_9b',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('9b')),
        ),
    ]
