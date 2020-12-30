from django.db import models

class AffiliateNetworks(models.Model):
    id = models.SmallAutoField(primary_key=True)
    public_id = models.CharField(unique=True, max_length=36)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    commission = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.IntegerField()
    purpose = models.ForeignKey('AffiliateNetworksPurposes', models.DO_NOTHING, blank=True, null=True)
    application_limit_per_day = models.PositiveSmallIntegerField(blank=True, null=True)
    accepts_conversion_limit = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'affiliate_networks'


class AffiliateNetworksPurposes(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'affiliate_networks_purposes'


class AffiliateUsers(models.Model):
    affiliate_network = models.ForeignKey(AffiliateNetworks, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.CharField(unique=True, max_length=180)
    roles = models.TextField()
    password = models.CharField(max_length=255)
    token_string = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.IntegerField()
    google_authenticator_secret = models.CharField(max_length=255, blank=True, null=True)
    is_google_authenticator_enabled = models.IntegerField(blank=True, null=True)
    last_2fa_code_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'affiliate_users'