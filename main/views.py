from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres, Artist, Albums, Tracks

from django.http import HttpResponseRedirect, JsonResponse

from main.models import CustomUser
from main.forms import UserSignUp, UserLogin

from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError


def ajax_search(request):
    context = {}
    return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))


def json_response(request):
    search_string = request.GET.get('search', '')

    objects = Artist.objects.filter(artist_name__icontains=search_string)

    object_list = []

    for obj in objects:
        object_list.append(obj.name)

    return JsonResponse(object_list, safe=False)


def signup(request):

    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':

        form = UserSignUp(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)

                auth_user = authenticate(email=email, password=password)

                login(request, auth_user)

                return HttpResponseRedirect('/')

            except IntegrityError, e:
                context['valid'] = "A USER WITH THAT NAME ALREADY EXIST"
        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):
    context = {}

    context['form'] = UserLogin()

    print "green"

    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            print "yellow"

            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                print "blue" 

                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Invalid User"
        else:
            context['valid'] = "Please enter a User Name"
    return render_to_response('registration/login.html', context, context_instance=RequestContext(request))


# This is for listing the objects
class GenreListView(ListView):
    model = Genres
    template_name = 'genres_list.html'
    context_object_name = 'genres'


# This is connecting the objects from the view???   
class GenreDetailView(DetailView):
    model = Genres
    template_name = 'genres_detail.html'
    context_object_name = 'genre'


# This is for forms
class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list/'


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artist'

    
# #class ArtistDetailView(DetailView):
#     model = Artist
#     template_name = 'artist_detail.html'
#     context_object_name = 'artist'


# #class ArtistCreateView(CreateView):
#     model = Artist
#     fields = '__all__'
#     template_name = 'artist_create.html'
#     success_url = '/artist_list/'


class AlbumListView(ListView):
    model = Albums
    template_name = 'albums_list.html'
    context_object_name = 'albums'

    

    




# class AlbumDetailView(DetailView):
#     model = Albums
#     template_name = 'albums_detail.html'


# class AlbumCreateView(CreateView):
#     model = Albums
#     fields = '__all__'
#     template_name = 'albums_create.html'
#     success_url = '/albums_list/'

class TrackListView(ListView):
    model = Tracks
    template_name = 'tracks_list.html'
    context_object_name = 'tracks'


# #class TrackDetailView(DetailView):
#     model = Tracks
#     template_name = 'tracks_detail.html'


# #class TrackCreateView(CreateView):
#     model = Tracks
#     fields = '__all__'
#     template_name = 'tracks_create.html'
#     success_url = '/tracks_list/'


def main_page(request):
        context = {}
        return render_to_response('main_page.html', context, context_instance=RequestContext(request))



