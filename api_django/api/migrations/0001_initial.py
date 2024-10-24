# Generated by Django 5.1.2 on 2024-10-24 21:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=30)),
                ('guest_lastname', models.CharField(max_length=30)),
                ('guest_age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18, message='La edad debe ser al menos 18 años')])),
                ('guest_email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Por favor, introduce un correo electrónico válido')])),
                ('guest_phonenumber', models.IntegerField()),
                ('guest_created_at', models.DateTimeField(auto_now_add=True)),
                ('guest_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1, message='El número de habitación debe ser un mayor a 1')])),
                ('room_type', models.CharField(max_length=100)),
                ('room_created_at', models.DateTimeField(auto_now_add=True)),
                ('room_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_number', models.IntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('reservation_created_at', models.DateTimeField(auto_now_add=True)),
                ('reservation_updated_at', models.DateTimeField(auto_now=True)),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.guest')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_number', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0, message='El número de review debe ser un número igual o mayor a 5'), django.core.validators.MaxLengthValidator(5, message='El número de review debe ser un número igual o menor a 5')])),
                ('review_comment', models.TextField(max_length=200)),
                ('review_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_updated_at', models.DateTimeField(auto_now=True)),
                ('reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reservation')),
            ],
        ),
    ]
