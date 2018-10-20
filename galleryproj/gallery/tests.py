from django.test import TestCase

import json

from . import s3lib

from .models import Photo, Like

class LikeModelTests(TestCase):
    def test_something(self):
        self.assertIs(True, True)

class PhotoModelTests(TestCase):
    def test_something(self):
        self.assertIs(True, True)

class S3Tests(TestCase):
    def test_sign(self):
        signature_str = s3lib.sign('hello','text')
        self.assertIs(type(signature_str)==str, True)
        
        signature = json.loads(signature_str)
        self.assertIs(type(signature)==type(dict()), True)
        self.assertIs(type(signature['url'])==type(''), True)
        self.assertIs(type(signature['data'])==type(dict()), True)
