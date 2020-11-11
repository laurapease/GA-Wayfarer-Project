from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    #-----STATIC
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #------ACCOUNT AND PROFILE
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/new/', views.new_profile, name='new_profile'),
    path('profile/<int:profile_id>/', views.user_profile, name='user_profile'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),

    #------POST
    path('city/<int:city_id>/add_post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('city/<slug:slug>/remove_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),

    #------CITIES

    path('cities/', views.cities_index, name='cities_index'),
    path('city/<slug:slug>/', views.view_city, name='view_city'),

    #------COMMENTS

    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:post_id>/remove_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)

