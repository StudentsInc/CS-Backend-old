from django.shortcuts import render
from rest_framework import viewsets, response, status, permissions
from .models import *
from .serializers import *


class BlogAPIView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        return response.Response(self.serializer_class(Blog.objects.all(), many=True).data, status=status.HTTP_200_OK)


class Latest_n_NumbersOfBlogAPIVIew(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def list(self, request, *args, **kwargs):
        if request.GET.get('number') is not None:
            self.queryset = Blog.objects.all()[:int(request.GET.get('number'))]
            if len(self.queryset) != int(request.GET.get('number')):
                return response.Response({'detail': f"{int(request.GET.get('number'))} blogs are not available in database."},
                                         status=status.HTTP_400_BAD_REQUEST)
            return response.Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)
        return response.Response({'detail': 'You must have to send a number in url to get the blogs.'},
                                 status=status.HTTP_400_BAD_REQUEST)


class RetriveBlogsBasedOnUserAPIView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        self.queryset = Blog.objects.filter(created_by=request.user)
        return response.Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)

