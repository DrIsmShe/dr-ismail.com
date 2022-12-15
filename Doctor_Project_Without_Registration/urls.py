"""Doktor_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap  # new
from django.contrib.sitemaps.views import sitemap  # new
from main.sitemaps import PostSitemap, StaticViewSitemap, AboutSitemap, AboutCategorySitemap, OurServiceSitemap, \
    OurServiceCategorySitemap, ImageGalleryCategorySitemap, PostCategorySitemap, VideoCategorySitemap, VideoSitemap
from main.models import Post, AboutDoctor, Category, ImageCategory, ImageGallery, CategoryAboutDoctor, \
    OurServicesCategory, OurServices

sitemaps = {
    'posts': PostSitemap,
    'sitemapsAbout': AboutSitemap,
    'sitemapsAboutCategory': AboutCategorySitemap,
    'sitemapsOurService': OurServiceSitemap,
    'sitemapsOurServiceCategory': OurServiceCategorySitemap,
    'sitemapsImageGalleryCategory': ImageGalleryCategorySitemap,
    'sitemapsPostCategory': PostCategorySitemap,
    'VideoCategorySitemap': VideoCategorySitemap,
    'VideoSitemap': VideoSitemap,
}

urlpatterns = [
    path('az/dr/ismail/admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('summernote/', include('django_summernote.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]

# pages, kotoriye nujno perevesti
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
)

handler404 = "main.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
