# Generated by Django 3.0.2 on 2020-12-30 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='affiliateuser',
            table='affiliate_users',
        ),
    ]