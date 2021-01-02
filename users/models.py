from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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


# class AffiliateUsers(models.Model):
#     affiliate_network = models.ForeignKey(AffiliateNetworks, models.DO_NOTHING, blank=True, null=True)
#     first_name = models.CharField(max_length=180)
#     last_name = models.CharField(max_length=180)
#     email = models.CharField(unique=True, max_length=180)
#     roles = models.TextField()
#     password = models.CharField(max_length=255)
#     token_string = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_enabled = models.IntegerField()
#     google_authenticator_secret = models.CharField(max_length=255, blank=True, null=True)
#     is_google_authenticator_enabled = models.IntegerField(blank=True, null=True)
#     last_2fa_code_used = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         db_table = 'affiliate_users'


class AffiliateUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AffiliateUser(AbstractBaseUser):
    affiliate_network = models.ForeignKey(AffiliateNetworks, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, db_index=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.TextField()
    password = models.CharField(max_length=255)
    token_string = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_enabled = models.IntegerField(default=True)
    google_authenticator_secret = models.CharField(max_length=255, blank=True, null=True)
    is_google_authenticator_enabled = models.IntegerField(blank=True, null=True)
    last_2fa_code_used = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AffiliateUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'affiliate_users'