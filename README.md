Photo Gallery
==

A collaborative photo gallery app. Demo: http://ciromoraismedeiros.pythonanywhere.com/

It is written in Django and uses AWS S3 to store photo files.

How it works
--
This is a collaborative photo gallery for a wedding.

Users are able to upload their photos to a unified gallery with all friend's photos.
The couple wants to approve the photos before they become visible to everyone.
Husband and wife are the only ones able to approve new photos.
Users must be able to like photos, and also sort them by total of likes or by date taken.

To add permission for approving photos, the user administrator must add husband and wife to the 'couple' group on the /admin pages.

Prerequisites
--
To run this application, you must have an AWS S3 bucket and user properly configured.

How to run locally
--
*Download source and install dependencies (use a virtual environment)

git clone https://github.com/ciromoraismedeiros/image-gallery.git

python -m pip install -r image-gallery/galleryproj/requirements.txt

*Django migrate database:

python image-gallery/galleryproj/manage.py makemigrations

python image-gallery/galleryproj/manage.py migrate

Run Django application with environment variables:

env BUCKET='your-bucket' AWS_ACCESS_KEY_ID='your-key' AWS_SECRET_ACCESS_KEY='your-secret' python image-gallery/galleryproj/manage.py runserver


Done! Access your server at localhost:8000

How to run tests
--
env BUCKET='your-bucket' AWS_ACCESS_KEY_ID='your-key' AWS_SECRET_ACCESS_KEY='your-secret' python image-gallery/galleryproj/manage.py test
