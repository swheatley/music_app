#!/usr/bin/env python
import requests
from unidecode import unidecode   
import os, sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings 
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


from main.models import Artist, Albums

django.setup()

for album in Albums.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 50, 'album_title': album.album_title}

    response = requests.get('http://freemusicarchive.org/api/get/artists.json', params=param_dict)

    response_dict = response.json()

    for data in response_dict['dataset']:

        artist, created = Artist.objects.get_or_create(artist_id=(data.get('artist_id')))
        artist.artist_url = str(data['artist_url'])

        if data.get('artist_bio') != None:
                artist.artist_bio = str(unidecode(data['artist_bio']))

        #artist.artist_website = str(data['artist_website'])
        #artist.artist_location = str(data['artist_location'])
                artist.artist_favorites = str(data['artist_favorites'])
                artist.artist_handle = str(data['artist_handle'])

        if data.get('artist_name') != None:
            artist.artist_name = str(unidecode(data.get('artist_name')))
        elif data.get('artist_name') == '(none given)':
            artist.artist_name = "none"
        else:
            artist.artist_name = " "

        if data.get('artist_website') != None:
            artist.artist_website = str(unidecode(data.get('artist_website')))


            # #if data['artist_name'] == None:
            #     return none

            # Artist location does not always populate
            # Artist name does not always populate
            # Artist website does not always populate

            #print data['artist_id']
        print artist.artist_name

        artist.save()


   
    # #print data['genre_title']
    # print data['genre_handle']
    # print data['genre_id']
    # print data ['genre_parent_id']



