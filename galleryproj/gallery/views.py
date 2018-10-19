from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import s3lib

def index(request):
    return render(request, 'home.html')

def sign_s3(request):
    filename = s3lib.generate_id()
    # filename = request.GET['file-name']
    filetype = request.GET['file-type']
    return HttpResponse(s3lib.sign(filename,filetype))

def submit_form(request):
    # Collect the data posted from the HTML form in upload.html:
    username = request.POST["username"]
    full_name = request.POST["full-name"]
    aws_img_url = request.POST["img-url"]
 
    # Provide some procedure for storing the new details

    # Redirect to the user's profile page, if appropriate
    return HttpResponseRedirect(reverse('home'))#, args=(question.id,)))

def upload(request):
    return render(request, 'upload.html')
