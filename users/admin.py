from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import AffiliateUser
import users.utils as utils


class AffiliateUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ('AffiliateUser', {'fields': ('affiliate_network', 'first_name', 'last_name', 'email',
                                      'username', 'is_admin', 'is_active', 'is_staff', 'is_superuser',
                                      'password', 'is_enabled')}),
    )

    def save_model(self, request, obj, form, change):
        obj.token_string = utils.generate_token()
        return super(AffiliateUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(AffiliateUser, AffiliateUserAdmin)
