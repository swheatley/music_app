#!/usr/bin/env python
import requests
import os, sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


from main.models import Genres, Tracks

django.setup()



for genre in Genres.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 50, 'genre_title': genre.genre_title }

    response = requests.get('http://freemusicarchive.org/api/get/genres.json' ,  params=param_dict)

    response_dict = response.json()


    for data in response_dict['dataset']:
        new_genre, created = Genres.objects.get_or_create(genre_title=data['genre_title'])

        new_genre.genre_handle = data['genre_handle']
        new_genre.genre_id = data['genre_id']
        new_genre.genre_parent_id = data['genre_parent_id']

        print data['genre_title']
        new_genre.save()

       
        print data['genre_title']
        print data['genre_handle']
        print data['genre_id']
        print data ['genre_parent_id']


