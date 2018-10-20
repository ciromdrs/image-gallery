Photo Gallery
==

A collaborative photo gallery app. Demo: http://ciromoraismedeiros.pythonanywhere.com/

It is written in Django and uses AWS S3 to store photo files.

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
