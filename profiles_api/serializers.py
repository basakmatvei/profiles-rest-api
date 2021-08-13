from rest_framework import serializers

from profiles_api import models


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Directory
        fields = ('ident', 'name', 'short_name', 'description', 'version', 'start_date')


class DirectoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DirectoryItem
        fields = ('id', 'parent', 'element_code', 'value')
