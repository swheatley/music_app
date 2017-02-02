#!/usr/bin/env python

import django
import sys
import os
import requests
from unidecode import unidecode
from PIL import Image


# .. looks up one directory
sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.conf import settings

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Albums, Artist, Genres, Tracks

django.setup()


for album in Tracks.objects.all():

    param_dict = {'api_key': settings.FMAKEY,'limit': 50, 'album_id': album.album_id }


    response = requests.get('http://freemusicarchive.org/api/get/albums.json' , params=param_dict)
    #requests.get('http://freemusicarchive.org/api/get/albums.json?_api_key=%s&limit=100artist_id=%' % (settings.FMAKEY, artist.artist_id)

    #required=Trueesponse_dict = response.json()
    response_dict = response.json()

    for data in response_dict['dataset']:
        print "IMAGE: %s" % data.get('album_image_file')
        print "TITLE: %s" % data.get('album_title')
        print "ARTIST: %s" % data.get('artist_name')
        print "ARTIST HANDLE: %s" % data.get('artist_handle')

        album, created = Albums.objects.get_or_create(album_id=data.get('album_id'))

        if data.get('album_title') != None:
            album.album_title = str(unidecode(data.get('album_title')))

        try:
            album_image = requests.get(data.get('album_image'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(album_image.content)
            img_name = "%s_album_img.jpg" % album.album_id
            album.album_image.save(img_name, File(temp_image))
        except Exception, e:
            print e

        album.save()


