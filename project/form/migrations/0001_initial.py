# Generated by Django 5.0.4 on 2024-05-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100)),
                ('form_email', models.EmailField(max_length=100)),
                ('form_number', models.CharField(max_length=100)),
                ('form_select', models.EmailField(max_length=100)),
            ],
        ),
    ]
