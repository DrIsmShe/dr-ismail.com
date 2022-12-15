# Generated by Django 4.1.1 on 2022-09-19 04:50

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of category')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name of category')),
                ('name_az', models.CharField(max_length=255, null=True, verbose_name='Name of category')),
                ('descriptions', models.TextField(verbose_name='Description of category')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of category')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetaKeywords of category')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of category')),
                ('image', models.ImageField(upload_to='category_post/', verbose_name='Image of category')),
            ],
            options={
                'verbose_name': 'Post Category',
                'verbose_name_plural': 'Post Categories ',
            },
        ),
        migrations.CreateModel(
            name='CategoryAboutDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of category')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name of category')),
                ('name_az', models.CharField(max_length=255, null=True, verbose_name='Name of category')),
                ('descriptions', models.TextField(verbose_name='Description of category')),
                ('descriptions_en', models.TextField(null=True, verbose_name='Description of category')),
                ('descriptions_az', models.TextField(null=True, verbose_name='Description of category')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of category')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetaKeywords of category')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of category')),
                ('image', models.ImageField(upload_to='category_about_doctor/', verbose_name='Image of category')),
            ],
            options={
                'verbose_name': 'About Doctor Category  ',
                'verbose_name_plural': 'About Doctor Categories ',
            },
        ),
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('title_en', models.CharField(blank=True, max_length=200, null=True)),
                ('title_az', models.CharField(blank=True, max_length=200, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image Category',
                'verbose_name_plural': 'Image Categories',
            },
        ),
        migrations.CreateModel(
            name='OurServicesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of AboutCategory')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name of AboutCategory')),
                ('name_az', models.CharField(max_length=255, null=True, verbose_name='Name of AboutCategory')),
                ('descriptions', models.TextField(verbose_name='Description of AboutCategory')),
                ('descriptions_en', models.TextField(null=True, verbose_name='Description of AboutCategory')),
                ('descriptions_az', models.TextField(null=True, verbose_name='Description of AboutCategory')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of AboutCategory')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetaKeywords of AboutCategory')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of AboutCategory')),
                ('image', models.ImageField(upload_to='about_category/', verbose_name='Image of AboutCategory')),
            ],
            options={
                'verbose_name': 'Our Services Category',
                'verbose_name_plural': 'Our Services Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Title of post')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Title of post')),
                ('title_az', models.CharField(max_length=155, null=True, verbose_name='Title of post')),
                ('tagline', models.CharField(default='', max_length=360, verbose_name='Tagline')),
                ('predescriptions', models.CharField(max_length=250, verbose_name='PreDescription')),
                ('descriptions', models.TextField(verbose_name='Description')),
                ('descriptions_en', models.TextField(null=True, verbose_name='Description')),
                ('descriptions_az', models.TextField(null=True, verbose_name='Description')),
                ('image_tur', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[200, 200], upload_to='Image_Tur//%Y/%m/%d', verbose_name='Poster of ListView')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Image//%Y/%m/%d', verbose_name='Poster of DetailView')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of movie')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetKeyWords of post')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of post')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('is_published', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date of published')),
                ('is_published_update', models.DateTimeField(auto_now=True, verbose_name='Date of update')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='RaitingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default='0', verbose_name='Rating in stars')),
            ],
            options={
                'verbose_name': 'Stars of rating',
                'verbose_name_plural': 'Stars of rating',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=125, verbose_name='Name of review')),
                ('text', models.TextField(max_length=5000, verbose_name='Text of review')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetaKeyWords of review')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescriptions of review')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post', verbose_name='Movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.reviews', verbose_name='Parent of review')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=25, verbose_name='IP of Rating')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post', verbose_name='Movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.raitingstar', verbose_name='Rating of movie')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Title of ourservices articles')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Title of ourservices articles')),
                ('title_az', models.CharField(max_length=155, null=True, verbose_name='Title of ourservices articles')),
                ('tagline', models.CharField(default='', max_length=360, verbose_name='Tagline')),
                ('predescriptions', models.CharField(max_length=250, verbose_name='PreDescription')),
                ('descriptions', models.TextField(verbose_name='Description')),
                ('descriptions_en', models.TextField(null=True, verbose_name='Description')),
                ('descriptions_az', models.TextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='ourservices/', verbose_name='Poster of ourservices articles')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of ourservices articles')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetKeyWords of ourservices articles')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of ourservices articles')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('is_published', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date of published')),
                ('is_published_update', models.DateTimeField(auto_now=True, verbose_name='Date of update')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ourservicescategory', verbose_name='Category of ourservices articles')),
            ],
            options={
                'verbose_name': 'Our service',
                'verbose_name_plural': 'Our services',
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=150, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_az', models.TextField(blank=True, null=True)),
                ('altText', models.TextField(blank=True, null=True)),
                ('hashtags', models.CharField(blank=True, max_length=300, null=True)),
                ('ImageList', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[200, 200], upload_to='Gallery/ImageList')),
                ('Image1', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image2', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image3', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image4', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image5', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image6', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image7', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image8', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image9', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image10', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image11', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpge', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image12', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image13', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image14', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image15', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image16', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image17', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image18', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image19', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image20', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image21', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image22', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image23', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('Image24', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Gallery')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.imagecategory')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='AboutDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Title of AboutDoctor')),
                ('title_en', models.CharField(max_length=155, null=True, verbose_name='Title of AboutDoctor')),
                ('title_az', models.CharField(max_length=155, null=True, verbose_name='Title of AboutDoctor')),
                ('tagline', models.CharField(default='', max_length=360, verbose_name='Tagline of AboutDoctor')),
                ('predescriptions', models.CharField(max_length=250, verbose_name='PreDescription of AboutDoctor')),
                ('descriptions', models.TextField(verbose_name='Description of AboutDoctor')),
                ('descriptions_en', models.TextField(null=True, verbose_name='Description of AboutDoctor')),
                ('descriptions_az', models.TextField(null=True, verbose_name='Description of AboutDoctor')),
                ('image_tur', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[200, 200], upload_to='Image_tur_About_Doctor', verbose_name='Poster of ListView of PostSingle')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='Image_About_Doctor', verbose_name='Poster of DetailView of AboutDoctor')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='URL of movie of AboutDoctor')),
                ('MetaKeyWords', models.CharField(max_length=500, verbose_name='MetKeyWords of AboutDoctor')),
                ('MetaDescriptions', models.CharField(max_length=500, verbose_name='MetaDescription of AboutDoctor')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('is_published', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date of published')),
                ('is_published_update', models.DateTimeField(auto_now=True, verbose_name='Date of update')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.categoryaboutdoctor', verbose_name='Category of AboutDoctor')),
            ],
            options={
                'verbose_name': 'About Doctor post',
                'verbose_name_plural': 'About Doctor posts',
            },
        ),
    ]
