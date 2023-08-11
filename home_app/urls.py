from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('banner', BannerAPIView)
router.register('our-skill', OurSkillAPIView)
router.register('about', AboutAPIView)
router.register('how-it-works', HowItWorksAPIView)
router.register('testimonials', TestimonialsAPIView)
router.register('brand', BrandAPIView)
router.register('contact-us', ContactUsAPIView)
router.register('testapi', TestAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('newsletter/', NewsletterAPIView.as_view()),
]

