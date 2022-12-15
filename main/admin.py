from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Post, OurServices, OurServicesCategory, ImageCategory, \
    ImageGallery, CategoryAboutDoctor, AboutDoctor, VideoCategory, Video
from django import forms
from embed_video.admin import AdminVideoMixin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Category
        fields = '__all__'




class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('id', 'name', 'url', 'MetaKeyWords', 'MetaDescriptions', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    form = CategoryCkeditorAdminForm


class PostAdmin(TranslationAdmin):
    list_display = (
        'id', 'title', 'category', 'MetaKeyWords', 'MetaDescriptions', 'draft',
        'is_published', 'image')
    list_editable = ('draft',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions', 'category')
    list_filter = ('title', 'category')
    prepopulated_fields = {'url': ('title',)}
    form = PostCkeditorAdminForm



class OurServicesCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = OurServices
        fields = '__all__'


class OurServicesCategoryCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = OurServicesCategory
        fields = '__all__'


class OurServicesCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('id', 'name', 'url', 'MetaKeyWords', 'MetaDescriptions', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    form = OurServicesCategoryCkeditorAdminForm


class OurServicesAdmin(TranslationAdmin):
    list_display = (
        'id', 'title', 'image', 'category', 'MetaKeyWords', 'MetaDescriptions', 'draft',
        'is_published')
    list_editable = ('draft',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions', 'category')
    list_filter = ('title', 'category')
    prepopulated_fields = {'url': ('title',)}
    form = OurServicesCkeditorAdminForm




class AboutDoctorCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutDoctor
        fields = '__all__'


class CategoryAboutDoctorCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = CategoryAboutDoctor
        fields = '__all__'

class CategoryAboutDoctorAdmin(TranslationAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('id', 'name', 'url', 'MetaKeyWords', 'MetaDescriptions', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    form = CategoryAboutDoctorCkeditorAdminForm


class AboutDoctorAdmin(TranslationAdmin):
    list_display = (
        'id', 'title', 'image', 'category', 'MetaKeyWords', 'MetaDescriptions', 'draft',
        'is_published')
    list_editable = ('draft',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions', 'category')
    list_filter = ('title', 'category')
    prepopulated_fields = {'url': ('title',)}
    form = AboutDoctorCkeditorAdminForm








class VideoCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Video
        fields = '__all__'


class CategoryVideoCkeditorAdminForm(forms.ModelForm):
    descriptions_az = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_ru = forms.CharField(widget=CKEditorUploadingWidget())
    descriptions_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = VideoCategory
        fields = '__all__'


class CategoryVideoAdmin(TranslationAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ('id', 'name', 'url', 'MetaKeyWords', 'MetaDescriptions', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    form = CategoryVideoCkeditorAdminForm


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = (
        'id', 'title', 'category', 'MetaKeyWords', 'MetaDescriptions', 'draft',
        'is_published', 'image_poster')
    list_editable = ('draft',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions', 'category')
    list_filter = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    form = VideoCkeditorAdminForm




class ImageCkeditorAdminForm(forms.ModelForm):
    description_az = forms.CharField(widget=CKEditorUploadingWidget())
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    description_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ImageGallery
        fields = '__all__'


class ImageCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ImageAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = ImageCkeditorAdminForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(OurServices, OurServicesAdmin)
admin.site.register(OurServicesCategory, OurServicesCategoryAdmin)
admin.site.register(ImageCategory, ImageCategoryAdmin)
admin.site.register(ImageGallery, ImageAdmin)
admin.site.register(AboutDoctor, AboutDoctorAdmin)
admin.site.register(CategoryAboutDoctor, CategoryAboutDoctorAdmin)
admin.site.register(VideoCategory, CategoryVideoAdmin)
admin.site.register(Video, VideoAdmin)
