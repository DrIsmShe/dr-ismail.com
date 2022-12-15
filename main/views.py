from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, OurServicesCategory, OurServices, ImageCategory, ImageGallery, AboutDoctor, \
    CategoryAboutDoctor, VideoCategory, Video
from django.db.models import Q
from django.conf import settings
from django.shortcuts import redirect



def page_not_found_view(request, exception):
    return render(request, 'html/404.html', status=404)


# otobrajeniye index.html
class PostViewIndex(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Вывод random статей на страницу  and Вывод определённого количества статей на страницу
        context['posts_for_index'] = Post.objects.all().order_by('?')[:15]
        context['posts_for_index_banner'] = Post.objects.all().order_by('?')[:3]
        context['categories_for_index'] = Category.objects.all().order_by('?')[:6]
        context['about_for_index'] = AboutDoctor.objects.all().order_by('?')[:6]
        context['our_service_last'] = OurServices.objects.all().order_by('?')[:6]
        context['categories'] = Category.objects.all()

        return context



# otobrajeniye statyi
class PostDetail(DetailView):
    def get(self, request, cat_url, post_url, post_id):
        PostDetail = get_object_or_404(Post, url=post_url, pk=post_id)
        category_item = get_object_or_404(Category, url=cat_url)
        MetaDescriptions = PostDetail.MetaDescriptions
        MetaKeyWords = PostDetail.MetaKeyWords
        title = PostDetail.title

        template_name = "post/post_detail.html"
        context = {
            'PostDetail': PostDetail,
            'category_item': category_item,
            'MetaDescriptions': MetaDescriptions,
            'MetaKeyWords': MetaKeyWords,
            'title': title,
        }
        return render(request, template_name, context)


# otobrajeniye category with posts
class CategoryPost(ListView):
    paginate_by = 6
    model = Post
    template_name = 'post/post_of_category.html'
    context_object_name = 'Category_Post'

    def get_queryset(self):
        object_filter = Post.objects.filter(category__url=self.kwargs['cat_url']).order_by('-id')
        return object_filter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['MetaDescriptions'] = 'Deaseses of ENT'
        context['MetaKeyWords'] = 'Deaseses of ENT'
        context['post_count'] = Post.objects.count()
        context['postcategory'] = Category.objects.filter(url=self.kwargs['cat_url']).order_by('name')

        return context


# otobrajeniye category with AboutCategory
class OurServicesCategory(ListView):
    paginate_by = 6
    model = OurServices
    template_name = 'ourservices/our_services_category.html'
    context_object_name = 'Our_Services_Category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Deaseses of ENT'
        context['MetaDescriptions'] = 'Deaseses of ENT'
        context['MetaKeyWords'] = 'Deaseses of ENT'

        return context

    def get_queryset(self):
        object_filter = OurServices.objects.filter(category__url=self.kwargs['ourservices_cat_url'], draft=False)

        return object_filter


# otobrajeniye statyi AboutDetail
class OurServicesDetail(DetailView):
    def get(self, request, ourservices_url, ourservices_id):
        ourservices = get_object_or_404(OurServices, url=ourservices_url, pk=ourservices_id)
        MetaDescription = ourservices.MetaDescriptions
        MetaKeyWords = ourservices.MetaKeyWords
        title = ourservices.title
        template_name = "ourservices/our_services_detail.html"
        context = {
            'ourservices': ourservices,
            'MetaDescription': MetaDescription,
            'MetaKeyWords': MetaKeyWords,
            'title': title,
        }
        return render(request, template_name, context)


def Home_Image(request):
    image_categories = ImageCategory.objects.all()

    context = {}
    context['categories'] = image_categories

    return render(request, 'image_temp/index.html', context)


def ImageCategoryPage(request, slug):
    image_gallery = ImageGallery.objects.all()
    paginator = Paginator(image_gallery, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    image_category = ImageCategory.objects.get(slug=slug)
    images = ImageGallery.objects.filter(category=image_category).order_by('-date_created')[:16]
    images_cat = ImageGallery.objects.filter(category__slug=slug)
    # for x in images:
    #     x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['images_cat'] = images_cat
    context['category'] = image_category
    context['page_obj'] = page_obj
    context['name'] = 'Deaseses of ENT'
    context['MetaDescriptions'] = 'Deaseses of ENT'
    context['MetaKeyWords'] = 'Deaseses of ENT'

    return render(request, 'image_temp/image_category.html', context)


def ImageDetailPage(request, slug1, slug2):
    image_category = ImageCategory.objects.get(slug=slug1)
    image = ImageGallery.objects.get(slug=slug2)



    MetaDescription = image.altText
    MetaKeyWords = image.hashtags
    title = image.title
    template_name = 'image_temp/image_detail.html'
    context = {
        'image': image,
        'category': image_category,
        'MetaDescription': MetaDescription,
        'MetaKeyWords': MetaKeyWords,
        'title': title,
    }
    return render(request, template_name, context)


# otobrajeniye statyi AboutDoctor
class AboutDoctorDetail(DetailView):
    def get(self, request, about_doctor_url, about_doctor_id):
        aboutdoctor = get_object_or_404(AboutDoctor, url=about_doctor_url, pk=about_doctor_id)
        aboutdoctorall = AboutDoctor.objects.all()
        MetaDescription = aboutdoctor.MetaDescriptions
        MetaKeyWords = aboutdoctor.MetaKeyWords
        title = aboutdoctor.title
        template_name = "about_doctor/about_doctor_detail.html"
        context = {
            'aboutdoctor': aboutdoctor,
            'aboutdoctorall': aboutdoctorall,
            'MetaDescription': MetaDescription,
            'MetaKeyWords': MetaKeyWords,
            'title': title,
        }
        return render(request, template_name, context)


# otobrajeniye category with AboutDoctor
class CategoryAboutDoctor(ListView):
    paginate_by = 1
    model = AboutDoctor
    template_name = 'about_doctor/about_doctor_of_category.html'
    context_object_name = 'about_doctor_category'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Deaseses of ENT'
        context['MetaDescriptions'] = 'Deaseses of ENT'
        context['MetaKeyWords'] = 'Deaseses of ENT'
        return context

    def get_queryset(self):
        object_filter = AboutDoctor.objects.filter(category__url=self.kwargs['cat_about_doctor_url'], draft=False)

        return object_filter






# contact html
def Contact(request):
    template_name = 'html/contact.html'
    title = 'Contact'
    context = {
        'title': title
    }
    return render(request, template_name, context)


# contact html
def FAQ(request):
    template_name = 'html/faq.html'
    title = 'Frequently asked questions - FAQ'
    context = {
        'title': title
    }
    return render(request, template_name, context)


class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 555

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(descriptions__icontains=query))
        return object_list


# otobrajeniye statyi
class VideoDetail(DetailView):
    def get(self, request, video_cat_url, video_url, video_id):
        VideoDetail = get_object_or_404(Video, slug=video_url, pk=video_id)
        video_category_item = get_object_or_404(VideoCategory, url=video_cat_url)
        MetaDescriptions = VideoDetail.MetaDescriptions
        MetaKeyWords = VideoDetail.MetaKeyWords
        title = VideoDetail.title

        template_name = "video/video_detail..html"
        context = {
            'VideoDetail': VideoDetail,
            'category_item': video_category_item,
            'MetaDescriptions': MetaDescriptions,
            'MetaKeyWords': MetaKeyWords,
            'title': title,
        }
        return render(request, template_name, context)


# otobrajeniye category with posts
class CategoryVideo(ListView):
    paginate_by = 5
    model = Video
    template_name = 'video/video_of_category.html'
    context_object_name = 'Category_Video'

    def get_queryset(self):
        object_filter = Video.objects.filter(category__url=self.kwargs['video_cat_url']).order_by('-id')
        return object_filter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['MetaDescriptions'] = 'Deaseses of ENT'
        context['MetaKeyWords'] = 'Deaseses of ENT'
        context['post_count'] = Video.objects.count()
        context['postcategory'] = VideoCategory.objects.filter(url=self.kwargs['video_cat_url']).order_by('name')

        return context
