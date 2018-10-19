from django.db import models

class Photo(models.Model):
    label = models.CharField(max_length=200)
    s3url = models.URLField(default='')

    def __str__(self):
        return self.label+":"+self.s3url
    
