Photo Gallery
==

A collaborative photo gallery app.
It is written in Django and uses AWS S3 to store photo files.

Prerequisites
--
To run this application, you must have an AWS S3 bucket, AWS user and a Google App Engine application (using python flexible environment) properly configured.

How to run locally
--
Create and configure a python3 virtual environment:

python3 -m venv env


Activate the virtual environment:

source env/bin/activate


Change to the env directory and clone this repository:

cd env/

git clone https://github.com/ciromoraismedeiros/image-gallery.git


(Optional) Upgrade pip:

python -m pip install --upgrade pip


Install project's requirements:

python -m pip install -r image-gallery/galleryproj/requirements.txt


(There is a default database included, so this command is optional) Django migrate database:

python image-gallery/galleryproj/manage.py migrate


Run Django application with environment variables:

env BUCKET='your-bucket' AWS_ACCESS_KEY_ID='your-key' AWS_SECRET_ACCESS_KEY='your-secret' python image-gallery/galleryproj/manage.py runserver


Done! Access your server at localhost:8000


How to deploy to Google App Engine flexible environment
--
Fill in the app.yaml configurations with your data.
You might also need to allow the App Engine host in Django's ALLOWED_HOSTS in the galleryproj/settings.py file.

gcloud app deploy




How to run tests
--
env BUCKET='your-bucket' AWS_ACCESS_KEY_ID='your-key' AWS_SECRET_ACCESS_KEY='your-secret' python image-gallery/galleryproj/manage.py test
