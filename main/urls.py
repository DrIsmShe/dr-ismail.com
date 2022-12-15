from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import Contact, FAQ

urlpatterns = [
    # cache_page(60*15)   )

    # path("", cache_page(60*15)(views.PostViewIndex.as_view()), name='home'),
    #
    # path("contact", cache_page(60*15)(Contact), name='contact'),
    # path("frequently-asked-questions", cache_page(60*15)(FAQ), name='faq'),
    #
    # path("search/", cache_page(60 * 15)(views.Search.as_view()), name='search'),
    #
    # path('video/<slug:video_cat_url>/<slug:video_url>/<int:video_id>', cache_page(60 * 15)(views.VideoDetail.as_view()),
    #      name='video_detail'),
    # path('videogallery/<slug:video_cat_url>', cache_page(60 * 15)(views.CategoryVideo.as_view()),
    #      name='video_category_list'),
    #
    # path('<slug:about_doctor_url>/<int:about_doctor_id>', cache_page(60*15)(views.AboutDoctorDetail.as_view()),
    #      name='about_doctor_detail'),
    # path('doctor/<slug:cat_about_doctor_url>', cache_page(60*15)(views.CategoryAboutDoctor.as_view()),
    #      name='about_doctor_of_category'),
    #
    # path('ourservices/<slug:ourservices_url>/<int:ourservices_id>',
    #      cache_page(60 * 15)(views.OurServicesDetail.as_view()), name='ourservices_detail'),
    # path('ourservices/<slug:ourservices_cat_url>', cache_page(60 * 15)(views.OurServicesCategory.as_view()),
    #      name='ourservices_category_list'),
    #
    # path('<slug:cat_url>/<slug:post_url>/<int:post_id>', cache_page(60 * 15)(views.PostDetail.as_view()),
    #      name='post_detail'),
    # path('ent/<slug:cat_url>', cache_page(60*15)(views.CategoryPost.as_view()), name='category_list'),
    #
    # path('images/', cache_page(60*15)(views.Home_Image), name='home_image'),
    # path('imagecategory/<slug:slug>', cache_page(60*15)(views.ImageCategoryPage), name='image-category'),
    # path('imagecategory/<slug:slug1>/<slug:slug2>', cache_page(60*15)(views.ImageDetailPage), name='image-detail'),

    path("", views.PostViewIndex.as_view(), name='home'),

    path("contact", Contact, name='contact'),
    path("frequently-asked-questions", FAQ, name='faq'),

    path("search/", views.Search.as_view(), name='search'),

    path('video/<slug:video_cat_url>/<slug:video_url>/<int:video_id>', views.VideoDetail.as_view(),
         name='video_detail'),
    path('videogallery/<slug:video_cat_url>', views.CategoryVideo.as_view(), name='video_category_list'),

    path('<slug:about_doctor_url>/<int:about_doctor_id>', views.AboutDoctorDetail.as_view(),
         name='about_doctor_detail'),
    path('doctor/<slug:cat_about_doctor_url>', views.CategoryAboutDoctor.as_view(),
         name='about_doctor_of_category'),

    path('ourservices/<slug:ourservices_url>/<int:ourservices_id>',
         views.OurServicesDetail.as_view(), name='ourservices_detail'),
    path('ourservices/<slug:ourservices_cat_url>', views.OurServicesCategory.as_view(),
         name='ourservices_category_list'),

    path('article/<slug:cat_url>/<slug:post_url>/<int:post_id>', views.PostDetail.as_view(),
         name='post_detail'),
    path('ent/<slug:cat_url>', views.CategoryPost.as_view(), name='category_list'),

    path('images/', views.Home_Image, name='home_image'),
    path('imagecategory/<slug:slug>', views.ImageCategoryPage, name='image-category'),
    path('imagecategory/<slug:slug1>/<slug:slug2>', views.ImageDetailPage, name='image-detail'),

]
