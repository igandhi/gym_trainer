# Generated by Django 2.0.3 on 2018-03-29 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Routine')),
            ],
        ),
    ]