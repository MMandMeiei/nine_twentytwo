# Generated by Django 3.0.2 on 2020-01-29 10:01

from django.db import migrations, models
import verification.models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_auto_20200126_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='chromosome_22c',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('22c')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_22d',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('22d')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_9c',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('9c')),
        ),
        migrations.AddField(
            model_name='image',
            name='chromosome_9d',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('9d')),
        ),
        migrations.AlterField(
            model_name='image',
            name='result_image',
            field=models.ImageField(blank=True, null=True, upload_to=verification.models.ImagePath('result')),
        ),
    ]
