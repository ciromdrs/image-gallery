from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import s3lib

def index(request):
    #  msg = "Hello, world. You're at the polls index.\n\n"
    #  url = s3lib.sign_s3('teste','txt')
    return render(request, 'home.html')

def sign_s3(request):
    print(__name__)
    filename = request.GET['file-name']
    filetype = request.GET['file-type']
    return HttpResponse(s3lib.sign(filename,filetype))

def submit_form(request):
    print(__name__)
    # Collect the data posted from the HTML form in account.html:
    username = request.POST["username"]
    full_name = request.POST["full-name"]
    aws_img_url = request.POST["img-url"]
 
    # Provide some procedure for storing the new details

    # Redirect to the user's profile page, if appropriate
    return HttpResponseRedirect(reverse('done'))#, args=(question.id,)))
