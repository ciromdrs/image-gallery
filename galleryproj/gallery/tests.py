from django.test import TestCase

import json

from . import s3lib

from .models import Photo, Like
from django.contrib.auth import get_user_model

User = get_user_model()

class GalleryTestCase(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice',
            'alice@example.com', 'password')

    def tearDown(self):
        User.objects.all().delete()
        Photo.objects.all().delete()

class PhotoTests(GalleryTestCase):
    def test_save_get_photo(self):
        '''Save and get a Photo'''
        label = 'this is the photo label'
        s3url = 'example.com'
        
        created = Photo.objects.create(owner=self.alice,label=label, s3url=s3url)
        
        photo = Photo.objects.get(id=created.id)

        self.assertEqual(self.alice,photo.owner)
        self.assertEqual(label,photo.label)
        self.assertEqual(s3url,photo.s3url)

    def test_like_photo(self):
        '''Like a photo'''
        

class S3Tests(GalleryTestCase):
    def test_sign(self):
        '''AWS S3 signature'''
        signature_str = s3lib.sign('hello','text')
        self.assertIs(type(signature_str)==str, True)
        
        signature = json.loads(signature_str)
        self.assertIs(type(signature)==type(dict()), True)
        self.assertIs(type(signature['url'])==type(''), True)
        self.assertIs(type(signature['data'])==type(dict()), True)
