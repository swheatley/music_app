#!/usr/bin/env python
import requests
from unidecode import unidecode   
import sys, os

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Tracks, Albums, Artist, Genres

django.setup()

for genre in Genres.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 50, 'genre_title': genre.genre_title}

    response = requests.get('http://freemusicarchive.org/api/get/tracks.json', params=param_dict)
    response_dict = response.json()

    for data in response_dict['dataset']:

        new_track, created = Tracks.objects.get_or_create(track_title=data.get('track_title'))
        new_track.track_id = data.get('track_id')

        new_track.album = data.get('album')
        new_track.genres = data.get('genres') 

        print new_track.track_title 

       












