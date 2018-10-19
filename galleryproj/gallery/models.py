from django.db import models

class Photo(models.Model):
    label = models.CharField(max_length=200)
    
