# Generated by Django 5.1.4 on 2025-02-08 07:42

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54, verbose_name='Имя')),
                ('position', models.CharField(choices=[('Мастер П/О', 'Мастер П/О'), ('Преподователь', 'Преподователь'), ('Учебная часть', 'Учебная часть'), ('Директор', 'Директор'), ('Заместитель директора', 'Заместитель директора')], default='Преподователь', max_length=21, verbose_name='Должность')),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
