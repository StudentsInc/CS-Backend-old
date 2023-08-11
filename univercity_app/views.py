from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response, status, viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CountryAPIView(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(Country, pk=kwargs['pk'])
        serializer = self.serializer_class(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        query = get_object_or_404(Country, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Country deleted successfully.'})


class MajorSetupAPIView(viewsets.ModelViewSet):
    serializer_class = MajorSetupSerializer
    queryset = MajorSetup.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = MajorSetup.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(MajorSetup, pk=kwargs['pk'])
        serializer = self.serializer_class(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        query = get_object_or_404(MajorSetup, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Major setup deleted successfully.'})


class SchoolProfileAPIView(viewsets.ModelViewSet):
    serializer_class = SchoolProfileSerializer
    queryset = SchoolProfile.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school_name', 'location']
    lookup_field = 'pk'

    # def list(self, request, *args, **kwargs):
    #     queryset = SchoolProfile.objects.all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolProfile, pk=kwargs['pk'])
        serializer = self.serializer_class(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolProfile, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'School profile deleted successfully.'})


class SchoolFilterAPIView(viewsets.ModelViewSet):
    serializer_class = SchoolProfileSerializer
    queryset = SchoolProfile.objects.all()
    pagination_class = StandardResultsSetPagination
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        country = request.data.get('country')
        major = request.data.get('major', None)
        if major:
            major = SchoolMajor.objects.filter(major=major, school__location=country).values_list('school', flat=True)
            query = self.get_queryset().filter(id__in=list(major))
            serializer = self.serializer_class(query, many=True)
            return Response(serializer.data)

        query = SchoolProfile.objects.filter(location=country)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class SchoolGalleryAPIView(viewsets.ModelViewSet):
    serializer_class = SchoolGallerySerializer
    queryset = SchoolGallery.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = SchoolGallery.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolGallery, pk=kwargs['pk'])
        serializer = self.serializer_class(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolGallery, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'School gallery deleted successfully.'})


class SchoolMajorAPIView(viewsets.ModelViewSet):
    serializer_class = SchoolMajorSerializer
    queryset = SchoolMajor.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = SchoolMajor.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolMajor, pk=kwargs['pk'])
        serializer = self.serializer_class(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        query = get_object_or_404(SchoolMajor, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'School major deleted successfully.'})


class UserSchoolView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SelectedSchool.objects.all()
    serializer_class = SelectedSchoolSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['created_by'] = request.user.id

        query = self.queryset.filter(created_by=request.user)
        if query:
            query.delete()
            ctx = {'message': 'School deleted.'}
            return Response(ctx)
        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
