from django.db.models import Q
from rest_framework import serializers


class QuerySetFilterMixin(object):

    def get_queryset(self):
        # This query is okay for Organization user
        # this query return data based on created by and mapped to related organization

        if self.request.user.is_superuser:
            queryset = super().get_queryset()
            return queryset

        queryset = super().get_queryset().filter(Q(created_by=self.request.user))
        return queryset

    def perform_create(self, serializer):
        serializer.created_by = self.request.user
        serializer.updated_by = self.request.user
        serializer.save()

    def perform_update(self, serializer):
        serializer.updated_by = self.request.user
        serializer.save()
