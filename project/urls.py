"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from django.views.generic.edit import CreateView

from main.forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),    
    url(r'^$', 'main.views.main_page', name='main_page'),

    # url(r'^', include('genres.urls')),
    # url(r'^$', views.GenreListView.as_view()),
    # url(r'^genres_detail/(?P<pk>\d+)/$', views.GenreDetailView.as_view()),

    
    url(r'^genres_list/$', views.GenreListView.as_view()),
    url(r'^genres_create/$', views.GenreCreateView.as_view()),

    url(r'^artist_list/$', views.ArtistListView.as_view()),
    # url(r'^artist_detail/(?P<pk>\d+)/$', views.ArtistDetailView()),
    # url(r'^artist_create/$', views.ArtistCreateView()),

    url(r'^albums_list/$', views.AlbumListView.as_view()),
    # url(r'^albums_detail/(?P<pk>\d+)/$', views.AlbumDetailView()),
    # url(r'^albums_create/$', views.AlbumCreateView()),

    url(r'^tracks_list/$', views.TrackListView.as_view()),
    # url(r'^tracks_detail/(?P<pk>\d+)/$', views.TrackDetailView()),
    # url(r'^tracks_create/$', views.TrackCreateView()),

    url(r'^signup/$', 'main.views.signup', name='signup_view'),
    url(r'^login/$', 'main.views.login_view', name='login_view'),
    url(r'^logout/$', 'main.views.logout_view', name='logout_view'),

    # url(r'^register/$', CreateView.as_view(template_name='register.html', form_class=CustomUserCreationForm, success_url='/')),
    # url(r'^ajax_search/$', 'main.views.ajax_search'),
    # url(r'^json_response/$', 'main.views.json_response'),

]


