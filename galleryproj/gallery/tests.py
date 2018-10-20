from django.test import TestCase, Client, SimpleTestCase
from django.test.utils import setup_test_environment
from django.urls import reverse
from django.db.utils import IntegrityError

import json

from . import s3lib

from .models import Photo, Like
from django.contrib.auth import get_user_model

client = Client() # Used to test views

User = get_user_model() # Avoid importing User model directly

class GalleryTestCase(TestCase):
    def setUp(self):
        '''Create useful data for tests'''
        #System users
        self.alice = User.objects.create_user('alice',
            'alice@example.com', 'password')
        self.bob = User.objects.create_user('bob',
            'bob@example.com', 'password')
        self.claire = User.objects.create_user('claire',
            'claire@example.com', 'password')
        self.david = User.objects.create_user('david',
            'david@example.com', 'password')

class PhotoTests(GalleryTestCase):
    def test_save_get_photo(self):
        '''Save and get a Photo'''
        label = 'this is the photo label'
        s3url = 'example.com'
        
        created = Photo.objects.create(owner=self.alice,label=label,
            s3url=s3url)
        
        photo = Photo.objects.get(id=created.id)

        self.assertEqual(self.alice,photo.owner)
        self.assertEqual(label,photo.label)
        self.assertEqual(s3url,photo.s3url)

    def test_like_photo_twice(self):
        '''Like a photo twice.'''
        label = 'photo to be liked'
        s3url = 'example.com'
        
        photo = Photo.objects.create(owner=self.alice,label=label,
            s3url=s3url)

        Like(user=self.alice,photo=photo).save()
        try:
            Like(user=self.alice,photo=photo).save()
            added_twice=True
        except IntegrityError:
            added_twice=False
        self.assertEquals(added_twice, False)

    def test_random_string(self):
        '''Random string generation.'''
        s1 = s3lib.generate_id()
        s2 = s3lib.generate_id()
        
        self.assertEquals(len(s1),20)
        self.assertEquals(len(s2),20)
        self.assertNotEquals(s1,s2)

    def test_sign(self):
        '''AWS S3 signature.'''
        signature_str = s3lib.sign('hello','text')
        self.assertIs(type(signature_str)==str, True)
        
        signature = json.loads(signature_str)
        self.assertEquals(type(signature),type(dict()))
        self.assertEquals(type(signature['url']),type(''))
        self.assertEquals(type(signature['data']),type(dict()))
    

class HomeViewTests(GalleryTestCase):
    def test_home_view(self):
        '''Serve home page.'''
        #TODO: test if logged in, redirect to see photos page.
        response = client.get(reverse('home'), follow=False)
        self.assertEqual(response.status_code, 200)

class SubmitPhotoViewTests(GalleryTestCase):
    def test_submit_photo(self):
        client.login(username=self.alice.username,password='password')
        response = client.post(reverse('submit'),{"label":'test photo',
            "img-url":'example.com/testphoto'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url.split('?')[0], reverse('upload'))
    


