from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import s3lib
from .models import Photo

def home(request):
    return render(request, 'home.html')

def sign_s3(request):
    filename = s3lib.generate_id()
    # filename = request.GET['file-name']
    filetype = request.GET['file-type']
    return HttpResponse(s3lib.sign(filename,filetype))

def submit_form(request):
    label = request.POST["label"]
    s3url = request.POST["img-url"]
    
    Photo(owner=request.user, label=label,s3url=s3url).save()

    return HttpResponseRedirect(reverse('home'))#, args=(question.id,)))

def upload(request):
    photos = Photo.objects.all() # TODO: filter photos by user
    return render(request, 'upload.html', {'photos':photos})
