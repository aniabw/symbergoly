# Generated by Django 3.0.2 on 2020-12-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]