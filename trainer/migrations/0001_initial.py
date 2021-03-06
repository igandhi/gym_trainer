# Generated by Django 2.0.3 on 2018-03-29 22:09

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_name', models.CharField(max_length=50)),
                ('random_url', models.UUIDField(default=uuid.uuid4)),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
