from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count

from . import s3lib
from .models import Photo, Like

def home(request):
    if request.user.is_authenticated:
        return redirect('see-photos')
    return render(request, 'home.html')

@login_required
def see_photos(request):
    sort = request.GET.get('sort','date')
    if sort == 'date':
        photos = Photo.objects.all().filter(approved=True).order_by('-upload_date')
    else:
        photos = Photo.objects.all().filter(approved=True).annotate(num_likes=Count('like')).order_by('-num_likes')
    for p in photos:
        p.liked = False
        for l in p.like_set.all():
            if request.user == l.user:
                p.liked = True
                break
    context = {'photos':photos, 'sort':sort}
    return render(request, 'see_photos.html', context)

@login_required
def sign_s3(request):
    filename = s3lib.generate_id()
    # filename = request.GET['file-name']
    filetype = request.GET['file-type']
    return HttpResponse(s3lib.sign(filename,filetype))

@login_required
def submit_form(request):
    label = request.POST["label"]
    s3url = request.POST["img-url"]
    
    Photo(owner=request.user, label=label,s3url=s3url).save()

    return redirect('upload')

@login_required
def upload(request):
    photos = Photo.objects.all().filter(owner=request.user).order_by('-upload_date')
    return render(request, 'upload.html', {'photos':photos})

@login_required
def like(request):
    if request.user.is_authenticated:
        l = Like(photo=Photo.objects.get(id=request.GET['photo-id']),
            user=request.user
        )
        l.save()
    # Redirect back, but preserve sorting
    response = redirect('see-photos')
    response['Location'] += '?sort='+request.GET['sort']
    return response

@login_required
def dislike(request):
    if request.user.is_authenticated:
        l = Like.objects.get(photo=Photo.objects.get(id=request.GET['photo-id']),
            user=request.user
        )
        l.delete()
    # Redirect back, but preserve sorting
    response = redirect('see-photos')
    response['Location'] += '?sort='+request.GET['sort']
    return response

@permission_required('gallery.approve_photo')
def approve(request):
    if request.method == 'GET':
        photos = Photo.objects.all().filter(approved=False)
        return render(request, 'approve.html', {'photos': photos})
    else:
        p = Photo.objects.get(id=request.POST['photo-id'])
        p.approved = True
        p.save()
        return redirect('approve')
    
