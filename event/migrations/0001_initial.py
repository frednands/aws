# Generated by Django 5.0.4 on 2024-06-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(default='/project/noimag.png', upload_to='event')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'managed': True,
            },
        ),
    ]
