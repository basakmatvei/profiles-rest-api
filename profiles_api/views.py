from django.http import Http404
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from profiles_api.models import DirectoryItem, Directory
from profiles_api.serializers import DirectorySerializer


class DirectoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DirectorySerializer
    queryset = models.Directory.objects.all()


class DirectoryItemsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DirectoryItemsSerializer
    queryset = DirectoryItem.objects.all()


class ItemsByDirectories(viewsets.ViewSet):

    def list(self, request, id):
        queryset = DirectoryItem.objects.filter(parent=id)
        serializer = serializers.DirectoryItemsSerializer(queryset, many=True)
        return Response(serializer.data)


class DirectoriesByTime(viewsets.ViewSet):

    def list(self, request, date):
        queryset = Directory.objects.filter(start_date__gt=date)
        serializer = serializers.DirectorySerializer(queryset, many=True)
        return Response(serializer.data)
