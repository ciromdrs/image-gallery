from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from . import s3lib
from .models import Photo, Like

def home(request):
    photos = Photo.objects.all().order_by('-upload_date')
    for p in photos:
        p.liked = False
        for l in p.like_set.all():
            if request.user == l.user:
                p.liked = True
                break
    return render(request, 'home.html', {'photos':photos})

def sign_s3(request):
    filename = s3lib.generate_id()
    # filename = request.GET['file-name']
    filetype = request.GET['file-type']
    return HttpResponse(s3lib.sign(filename,filetype))

def submit_form(request):
    label = request.POST["label"]
    s3url = request.POST["img-url"]
    
    Photo(owner=request.user, label=label,s3url=s3url).save()

    return redirect('home')#, args=(question.id,)))

def upload(request):
    photos = Photo.objects.all().filter(owner=request.user).order_by('-upload_date')
    return render(request, 'upload.html', {'photos':photos})

def like(request):
    l = Like(photo=Photo.objects.get(id=request.GET['photo-id']),
        user=request.user
    )
    l.save()
    return redirect('home')

def dislike(request):
    pass
    return redirect('home')
