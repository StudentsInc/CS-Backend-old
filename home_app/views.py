from django.shortcuts import render, get_object_or_404
from rest_framework import response, status, viewsets, generics,permissions
from .serializers import *
from .models import *


class BannerAPIView(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = Banner.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(Banner, pk=kwargs['pk'])
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
        query = get_object_or_404(Banner, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Banner deleted successfully.'})


class OurSkillAPIView(viewsets.ModelViewSet):
    serializer_class = OurSkillSerializer
    queryset = OurSkill.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = OurSkill.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(OurSkill, pk=kwargs['pk'])
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
        query = get_object_or_404(OurSkill, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Skill deleted successfully.'})


class AboutAPIView(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = About.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(About, pk=kwargs['pk'])
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
        query = get_object_or_404(About, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'About deleted successfully.'})


class HowItWorksAPIView(viewsets.ModelViewSet):
    serializer_class = HowItWorksSerializer
    queryset = HowItWorks.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = HowItWorks.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(HowItWorks, pk=kwargs['pk'])
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
        query = get_object_or_404(HowItWorks, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Works deleted successfully.'})


class TestimonialsAPIView(viewsets.ModelViewSet):
    serializer_class = TestimonialSerializer
    queryset = Testimonials.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = Testimonials.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(Testimonials, pk=kwargs['pk'])
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
        query = get_object_or_404(Testimonials, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Testimonials deleted successfully.'})


class BrandAPIView(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = Brand.objects.filter(status__exact='active')
        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        query = get_object_or_404(Brand, pk=kwargs['pk'])
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
        query = get_object_or_404(Brand, pk=kwargs['pk'])
        query.delete()
        return response.Response({'detail': 'Brand deleted successfully.'})


class ContactUsAPIView(viewsets.ModelViewSet):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors)


class NewsletterAPIView(generics.GenericAPIView):
    serializer_class = NewsletterSerializer

    def post(self, request):
        if 'email' not in request.data:
            return response.Response({'error': 'Please enter email id.'}, status=status.HTTP_400_BAD_REQUEST)
        if Newsletter.objects.filter(email=request.data['email']).exists():
            return response.Response({'Error': 'This email id is already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'detail': 'Subscription done!'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestAPIView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AboutSerializer
    queryset = About.objects.all()
