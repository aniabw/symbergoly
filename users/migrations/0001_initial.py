# Generated by Django 3.0.2 on 2020-12-30 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliateNetworksPurposes',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'affiliate_networks_purposes',
            },
        ),
        migrations.CreateModel(
            name='AffiliateNetworks',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('public_id', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('commission', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_enabled', models.IntegerField()),
                ('application_limit_per_day', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('accepts_conversion_limit', models.CharField(blank=True, max_length=15, null=True)),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.AffiliateNetworksPurposes')),
            ],
            options={
                'db_table': 'affiliate_networks',
            },
        ),
        migrations.CreateModel(
            name='AffiliateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=180)),
                ('last_name', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('roles', models.TextField()),
                ('password', models.CharField(max_length=255)),
                ('token_string', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_enabled', models.IntegerField()),
                ('google_authenticator_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('is_google_authenticator_enabled', models.IntegerField(blank=True, null=True)),
                ('last_2fa_code_used', models.CharField(blank=True, max_length=10, null=True)),
                ('affiliate_network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.AffiliateNetworks')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]