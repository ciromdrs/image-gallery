from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-s3/', views.sign_s3, name='sign-s3'),
    path('submit-form/', views.submit_form, name='submit'),
    path('', views.submit_form, name='done'),
]
