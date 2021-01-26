from django.contrib.auth.models import User
from apps.users.models import AffiliateUser
from rest_framework import authentication
from rest_framework import exceptions


class LoanableApiAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        affiliate_network = request.headers.get('X-Affiliate-Network')
        bearer = request.headers.get('Authorization')
        if bearer:
            bearer = bearer.partition(" ")[2]

        if not affiliate_network or not bearer:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        try:
            user = AffiliateUser.objects.get(token_string=bearer, affiliate_network_id__public_id=affiliate_network)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')  # raise exception if user does not exist

        return user, None  # authentication successful
