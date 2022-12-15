from modeltranslation.translator import register, TranslationOptions
from .models import Post, Category, ImageCategory, ImageGallery, \
    ResizedImageField, AboutDoctor, CategoryAboutDoctor, OurServicesCategory, OurServices, VideoCategory, Video


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('descriptions', 'title', 'tagline', 'MetaKeyWords', 'MetaDescriptions')


@register(OurServicesCategory)
class OurServicesCategoryTranslationOptions(TranslationOptions):
    fields = ('descriptions', 'name')


@register(OurServices)
class OurServicesTranslationOptions(TranslationOptions):
    fields = ('descriptions', 'title', 'tagline', 'MetaKeyWords', 'MetaDescriptions')


@register(ImageGallery)
class ImageGalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'hashtags')


@register(ImageCategory)
class ImageCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CategoryAboutDoctor)
class CategoryAboutDoctorTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(AboutDoctor)
class AboutDoctorTranslationOptions(TranslationOptions):
    fields = ('descriptions', 'title', 'tagline', 'MetaKeyWords', 'MetaDescriptions')


@register(VideoCategory)
class VideoCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'descriptions')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('descriptions', 'title', 'tagline', 'MetaKeyWords', 'MetaDescriptions')
