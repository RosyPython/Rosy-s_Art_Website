from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('a4', views.a4, name="a4"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]
