# Generated by Django 5.1.2 on 2024-10-31 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='estudante',
        ),
        migrations.AddField(
            model_name='estudante',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.professor'),
            preserve_default=False,
        ),
    ]
