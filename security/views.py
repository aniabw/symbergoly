from django.contrib.auth.models import User
from users.models import AffiliateUser
from rest_framework import authentication
from rest_framework import exceptions

class LoanableApiAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get('X-Affiliate-Network')

        if not username:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        try:
            user = AffiliateUser.objects.get(username=username)  # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')  # raise exception if user does not exist

        return user, None  # authentication successful
