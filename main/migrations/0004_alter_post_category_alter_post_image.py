# Generated by Django 4.1.1 on 2022-09-23 06:42

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutdoctor_descriptions_ru_aboutdoctor_title_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='category_post', to='main.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpeg', force_format=None, keep_meta=True, quality=75, scale=None, size=[500, 500], upload_to='Image//%Y/%m/%d', verbose_name='Poster of DetailView'),
        ),
    ]