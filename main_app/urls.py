from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/new/', views.new_profile, name='new_profile'),
    path('profile/<int:profile_id>/', views.user_profile, name='user_profile'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    path('post/new/', views.add_post, name="add_post"),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('cities/', views.cities_index, name='cities_index'),
    path('city/<int:city_id>', views.view_city, name='view_city'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)

