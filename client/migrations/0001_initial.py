# Generated by Django 5.0.4 on 2024-06-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, unique=True)),
                ('qoute', models.TextField(max_length=255)),
                ('image', models.FileField(upload_to='client/')),
            ],
        ),
    ]
