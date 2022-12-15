
from django import template
from main.models import Category, OurServicesCategory, ImageCategory, CategoryAboutDoctor, Post, OurServices, VideoCategory
import os
from django.core.files.storage import default_storage

register = template.Library()


@register.simple_tag()
def get_tagline_posts():
    return Post.objects.all().order_by('tagline')[:10]


@register.simple_tag()
def get_categories_ourservices():
    return OurServicesCategory.objects.all()


@register.simple_tag()
def get_posts():
    return Post.objects.all().order_by('-is_published')[:4]

@register.simple_tag()
def get_posts_banner():
    return Post.objects.all().order_by('-is_published')[:3]

@register.simple_tag()
def get_OurServices():
    return OurServices.objects.all().order_by('-is_published')[:4]


@register.simple_tag()
def get_categories_about_doctor():
    return CategoryAboutDoctor.objects.all()


@register.simple_tag()
def get_video_categories():
    return VideoCategory.objects.all()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_categories_image():
    return ImageCategory.objects.all()


@register.filter
def filename(value):
    return os.path.basename(value.file.name)


@register.filter
def file_exists(value):
    if default_storage.exists(value):
        return True
    else:
        return False
