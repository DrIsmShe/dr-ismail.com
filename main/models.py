from django.db import models
from django.urls import reverse

from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of category')
    descriptions = models.TextField(verbose_name='Description of category')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of category')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetaKeywords of category')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of category')
    image = models.ImageField(upload_to="category_post/", verbose_name='Image of category')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'cat_url': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories "


class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title of post')
    tagline = models.CharField(max_length=360, default="", verbose_name='Tagline')
    descriptions = models.TextField(verbose_name='Description')
    image_tur = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to="Image_Turb_Post//%Y/%m/%d",
                                  verbose_name='Poster of ListView', default='default.jpeg')
    image = ResizedImageField(size=[500, 500], crop=['middle', 'center'], default='default.jpeg',
                              upload_to='Image_Post//%Y/%m/%d', verbose_name='Poster of DetailView')
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True,
                                 related_query_name='category_post')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of Post')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetKeyWords of post')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of post')
    draft = models.BooleanField(verbose_name="Draft", default=False)
    is_published = models.DateTimeField(auto_now_add=True, verbose_name='Date of published', null=True)
    is_published_update = models.DateTimeField(auto_now=True, verbose_name='Date of update')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'cat_url': self.category.url, 'post_url': self.url, 'post_id': self.pk})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-id']


class OurServicesCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of AboutCategory')
    descriptions = models.TextField(verbose_name='Description of AboutCategory')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of AboutCategory')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetaKeywords of AboutCategory')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of AboutCategory')
    image = models.ImageField(upload_to="about_category/", verbose_name='Image of AboutCategory')

    def get_absolute_url(self):
        return reverse('ourservices_category_list', kwargs={'ourservices_cat_url': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Our Services Category"
        verbose_name_plural = "Our Services Categories"


class OurServices(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title of ourservices articles')
    tagline = models.CharField(max_length=360, default="", verbose_name='Tagline')
    predescriptions = models.CharField(max_length=250, verbose_name='PreDescription')
    descriptions = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to="ourservices/", verbose_name='Poster of ourservices articles')
    category = models.ForeignKey(OurServicesCategory, verbose_name="Category of ourservices articles",
                                 on_delete=models.SET_NULL,
                                 null=True)
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of ourservices articles')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetKeyWords of ourservices articles')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of ourservices articles')
    draft = models.BooleanField(verbose_name="Draft", default=False)
    is_published = models.DateTimeField(auto_now_add=True, verbose_name='Date of published', null=True)
    is_published_update = models.DateTimeField(auto_now=True, verbose_name='Date of update')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ourservices_detail',
                       kwargs={'ourservices_url': self.url, 'ourservices_id': self.pk})

    class Meta:
        verbose_name = "Our service"
        verbose_name_plural = "Our services"


class CategoryAboutDoctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of category')
    descriptions = models.TextField(verbose_name='Description of category')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of category')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetaKeywords of category')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of category')
    image = models.ImageField(upload_to="category_about_doctor/", verbose_name='Image of category')

    def get_absolute_url(self):
        return reverse('about_doctor_of_category', kwargs={'cat_about_doctor_url': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "About Doctor Category  "
        verbose_name_plural = "About Doctor Categories "


class AboutDoctor(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title of AboutDoctor')
    tagline = models.CharField(max_length=360, default="", verbose_name='Tagline of AboutDoctor')
    predescriptions = models.CharField(max_length=250, verbose_name='PreDescription of AboutDoctor')
    descriptions = models.TextField(verbose_name='Description of AboutDoctor')
    image_tur = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to="Image_tur_About_Doctor",
                                  verbose_name='Poster of ListView of PostSingle', default='default.jpeg')
    image = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                              upload_to='Image_About_Doctor', verbose_name='Poster of DetailView of AboutDoctor')
    category = models.ForeignKey(CategoryAboutDoctor, verbose_name="Category of AboutDoctor", on_delete=models.SET_NULL,
                                 null=True)
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of movie of AboutDoctor')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetKeyWords of AboutDoctor')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of AboutDoctor')
    draft = models.BooleanField(verbose_name="Draft", default=False)
    is_published = models.DateTimeField(auto_now_add=True, verbose_name='Date of published', null=True)
    is_published_update = models.DateTimeField(auto_now=True, verbose_name='Date of update')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_doctor_detail', kwargs={'about_doctor_url': self.url, 'about_doctor_id': self.pk})

    class Meta:
        verbose_name = "About Doctor post"
        verbose_name_plural = "About Doctor posts"


# class RaitingStar(models.Model):
#     value = models.PositiveIntegerField(verbose_name="Rating in stars", default="0", help_text="")
#
#     def __str__(self):
#         return self.value
#
#     class Meta:
#         verbose_name = "Stars of rating"
#         verbose_name_plural = "Stars of rating"
#
#
# class Raiting(models.Model):
#     ip = models.CharField(verbose_name="IP of Rating", max_length=25)
#     star = models.ForeignKey(RaitingStar, verbose_name='Rating of movie', on_delete=models.CASCADE)
#     movie = models.ForeignKey(Post, verbose_name="Movie", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.star}-{self.movie}"
#
#     class Meta:
#         verbose_name = "Rating"
#         verbose_name_plural = "Ratings"
#
#
# class Reviews(models.Model):
#     email = models.EmailField()
#     name = models.CharField(max_length=125, verbose_name='Name of review')
#     text = models.TextField(max_length=5000, verbose_name='Text of review')
#     parent = models.ForeignKey('self', verbose_name='Parent of review', on_delete=models.SET_NULL, null=True,
#                                blank=True)
#     movie = models.ForeignKey(Post, verbose_name="Movie", on_delete=models.CASCADE, related_name='comments')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)
#     MetaKeyWords = models.CharField(max_length=500, verbose_name='MetaKeyWords of review')
#     MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescriptions of review')
#
#     def __str__(self):
#         return f"{self.name}-{self.movie}"
#
#     class Meta:
#         verbose_name = "Review"
#         verbose_name_plural = "Reviews"
#         ordering = ('created',)


class ImageCategory(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('image-category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(ImageCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Image Category"
        verbose_name_plural = "Image Categories"


class ImageGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title', null=True)
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    ImageList = ResizedImageField(size=[200, 200], crop=['middle', 'center'], default='default.jpeg',
                                  upload_to='Gallery/ImageList')
    Image1 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image2 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image3 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image4 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image5 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image6 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image7 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image8 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image9 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                               upload_to='Gallery')
    Image10 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image11 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpge',
                                upload_to='Gallery')
    Image12 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image13 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image14 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image15 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image16 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image17 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image18 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image19 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image20 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image21 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image22 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image23 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')
    Image24 = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default.jpeg',
                                upload_to='Gallery')

    ##Related Fiels
    category = models.ForeignKey(ImageCategory, null=True, blank=True, on_delete=models.CASCADE)

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return '{} {}'.format(self.title, self.uniqueId)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class VideoCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of VideoCategory')
    descriptions = models.TextField(verbose_name='Description of VideoCategory')
    url = models.SlugField(max_length=160, unique=True, verbose_name='URL of VideoCategory')
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetaKeywords of VideoCategory')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of VideoCategory')
    image = models.ImageField(upload_to="Video/category_video", verbose_name='Image of VideoCategory')

    def get_absolute_url(self):
        return reverse('video_category_list', kwargs={'video_cat_url': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "VideoCategory"
        verbose_name_plural = "VideoCategory "


class Video(models.Model):
    title = models.CharField(max_length=155, verbose_name='Title of Video')
    tagline = models.CharField(max_length=360, default="", verbose_name='Tagline of Video')
    descriptions = models.TextField(verbose_name='Description of Video')
    image_poster = ResizedImageField(size=[500, 500], crop=['middle', 'center'], default='default.jpeg',
                                     upload_to='Video/image_poster', verbose_name='Poster of DetailView')
    video_youtube = models.CharField(max_length=1155, null=True, blank=True, verbose_name='Video from youtube')
    video_our = models.FileField(upload_to='Video/video_our', verbose_name='Video from our server', default='default.mp4')
    category = models.ForeignKey(VideoCategory, verbose_name="Category", on_delete=models.SET_NULL, null=True,
                                 related_query_name='category_video')

    url = EmbedVideoField()
    slug = models.SlugField(max_length=160, unique=True, verbose_name='URL of movie', null=True, blank=True)
    MetaKeyWords = models.CharField(max_length=500, verbose_name='MetKeyWords of video')
    MetaDescriptions = models.CharField(max_length=500, verbose_name='MetaDescription of video')
    draft = models.BooleanField(verbose_name="Draft", default=False)
    is_published = models.DateTimeField(auto_now_add=True, verbose_name='Date of published', null=True)
    is_published_update = models.DateTimeField(auto_now=True, verbose_name='Date of update')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail',
                       kwargs={'video_cat_url': self.category.url, 'video_url': self.slug, 'video_id': self.pk})

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['-id']
