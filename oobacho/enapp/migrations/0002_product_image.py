# Generated by Django 4.2.4 on 2023-12-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='mediafiles/'),
            preserve_default=False,
        ),
    ]
