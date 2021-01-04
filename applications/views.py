from applications.models import Application
from applications.serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from security.views import LoanableApiAuthentication
from rest_framework.response import Response

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows application to be viewed or edited.
    """
    authentication_classes = (LoanableApiAuthentication,)
    queryset = Application.objects.all().order_by('-created_at')
    serializer_class = ApplicationSerializer

    permission_classes = (IsAuthenticated,)

    # def list(self, request, pk=None):
    #     return Response({
    #             "applicationId": "45484428-4a8d-11eb-852e-0a237893ab20",
    #             "applicationType": "ShortTermLoan",
    #             "createdAt": "2020-12-30 10:53:37"
    #         })
