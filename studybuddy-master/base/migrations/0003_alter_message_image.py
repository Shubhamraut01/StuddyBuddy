# Generated by Django 4.0 on 2022-02-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='msgImages'),
        ),
    ]