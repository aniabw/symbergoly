from apps.applications.models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['public_id', 'amount', 'term']

