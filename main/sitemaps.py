from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post, AboutDoctor, Category, ImageCategory, ImageGallery, CategoryAboutDoctor, \
    OurServicesCategory, OurServices, VideoCategory, Video


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['Contact']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all()

class PostCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()


class AboutSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return AboutDoctor.objects.all()

class AboutCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return CategoryAboutDoctor.objects.all()

class OurServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return OurServices.objects.all()

class OurServiceCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return OurServicesCategory.objects.all()

class VideoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Video.objects.all()

class VideoCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return VideoCategory.objects.all()


class ImageGalleryCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ImageCategory.objects.all()