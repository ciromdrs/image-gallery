from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-s3/', views.sign_s3, name='sign-s3'),
    path('submit-form/', views.submit_form, name='submit'),
    path('upload/', views.upload, name='upload'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('approve/', views.approve, name='approve'),
]

