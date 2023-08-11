"""career_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Career Studio",
        default_version='v1',
        # description="Career Studio Backend",
    ),
    public=True
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account_app.urls')),
    path('api/v1/cms_app/', include('cms_app.urls')),
    path('api/v1/career/', include('career.urls')),
    path('api/v1/blogs/', include('blog.urls')),
    path('api/v1/home/', include('home_app.urls')),
    path('api/v1/about/', include('about_app.urls')),
    path('api/v1/educator/', include('educator_app.urls')),
    path('api/v1/dashboard/', include('dashboard_app.urls')),
    path('api/v1/counseling/', include('counseling_app.urls')),
    path('api/v1/interest/', include('interest_app.urls')),
    path('api/interest/', include('interest_app.urls')),
    path('api/v1/learning/', include('learning_style.urls')),
    path('api/v1/personality_test/', include('personality_test.urls')),
    path('api/v1/payment/', include('payment.urls')),
    path('api/v1/survey/', include('survey.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/career/', include('univercity_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
