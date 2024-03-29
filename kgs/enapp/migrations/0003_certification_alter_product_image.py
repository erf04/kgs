# Generated by Django 4.2.4 on 2023-12-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enapp', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='mediafiles/certification/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='mediafiles/product/'),
        ),
    ]
