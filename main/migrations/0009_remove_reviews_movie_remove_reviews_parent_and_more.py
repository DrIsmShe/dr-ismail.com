# Generated by Django 4.1.1 on 2022-09-28 12:09

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_post_image_alter_post_image_tur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
        migrations.AlterField(
            model_name='aboutdoctor',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Image_About_Doctor', verbose_name='Poster of DetailView of AboutDoctor'),
        ),
        migrations.AlterField(
            model_name='aboutdoctor',
            name='image_tur',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[200, 200], upload_to='images_for_site/Image_tur_About_Doctor', verbose_name='Poster of ListView of PostSingle'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images_for_site/category_post/', verbose_name='Image of category'),
        ),
        migrations.AlterField(
            model_name='categoryaboutdoctor',
            name='image',
            field=models.ImageField(upload_to='images_for_site/category_about_doctor/', verbose_name='Image of category'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image1',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image10',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image11',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpge', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image12',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image13',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image14',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image15',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image16',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image17',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image18',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image19',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image2',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image20',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image21',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image22',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image23',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image24',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image3',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image4',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image5',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image6',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image7',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image8',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='Image9',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='images_for_site/Gallery'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='ImageList',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[200, 200], upload_to='images_for_site/Gallery/ImageList'),
        ),
        migrations.AlterField(
            model_name='ourservices',
            name='image',
            field=models.ImageField(upload_to='images_for_site/ourservices/', verbose_name='Poster of ourservices articles'),
        ),
        migrations.AlterField(
            model_name='ourservicescategory',
            name='image',
            field=models.ImageField(upload_to='images_for_site/about_category/', verbose_name='Image of AboutCategory'),
        ),
        migrations.DeleteModel(
            name='Raiting',
        ),
        migrations.DeleteModel(
            name='RaitingStar',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
