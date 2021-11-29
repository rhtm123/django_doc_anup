from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import HttpResponse

from blog import views

urlpatterns = [
    path("", views.blog_home),
    path("<int:pk>/", views.single_blog),
]
